import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid


class DataGenerator:
    """Generate realistic food delivery data."""
    
    CUISINES = ["Italian", "Chinese", "Mexican", "Japanese", "Thai", 
                "Vietnamese", "Fast Food", "Pizza", "Sushi"]
    
    def __init__(self, date=None, customers=500, restaurants=100, orders=2000):
        self.date = date or datetime.now()
        self.num_customers = customers
        self.num_restaurants = restaurants
        self.num_orders = orders
        
    def _demand_at_hour(self, hour):
        """Return order multiplier for peak/off-peak hours."""
        if 7 <= hour < 10:
            return 0.8  # Breakfast
        elif 12 <= hour < 14:
            return 2.1  # Lunch
        elif 18 <= hour < 21:
            return 1.4  # Dinner
        elif hour < 7 or hour >= 23:
            return 0.2  # Night
        else:
            return 0.5  # Regular
    
    def generate_customers(self):
        """Generate customer data."""
        return pd.DataFrame({
            'customer_id': [f"CUST_{uuid.uuid4().hex[:10].upper()}" for _ in range(self.num_customers)],
            'zone': np.random.choice(["North", "South", "East", "West"], self.num_customers, p=[0.45, 0.07, 0.33, 0.15]),
            'latitude': np.random.uniform(40.7, 40.9, self.num_customers),
            'longitude': np.random.uniform(-74.0, -73.9, self.num_customers),
            'tier': np.random.choice(["bronze", "silver", "gold"], self.num_customers, p=[0.5, 0.35, 0.15]),
            'signup_date': [(self.date - timedelta(days=int(np.random.exponential(180)))).date() for _ in range(self.num_customers)],
            'is_active': np.random.choice([True, False], self.num_customers, p=[0.65, 0.35])
        })
    
    def generate_restaurants(self):
        """Generate restaurant data."""
        # Weighted cuisine distribution (some cuisines more popular)
        cuisine_weights = np.array([0.15, 0.12, 0.10, 0.11, 0.10, 0.09, 0.13, 0.12, 0.08])
        cuisines = np.random.choice(self.CUISINES, self.num_restaurants, p=cuisine_weights)
        
        # Beta distribution for ratings (skewed towards higher values: 3.5-4.8)
        ratings = np.random.beta(8, 2, self.num_restaurants) * 1.8 + 2.9
        
        # Gamma distribution for delivery times (realistic skew around mean ~25 min)
        delivery_times = np.random.gamma(shape=2.5, scale=10, size=self.num_restaurants)
        
        return pd.DataFrame({
            'restaurant_id': [f"REST_{uuid.uuid4().hex[:8].upper()}" for _ in range(self.num_restaurants)],
            'name': [f"{cuisine} #{i}" for i, cuisine in enumerate(cuisines)],
            'cuisine': cuisines,
            'zone': np.random.choice(["North", "South", "East", "West"], self.num_restaurants, p=[0.4, 0.1, 0.3, 0.2]),
            'latitude': np.random.uniform(40.7, 40.9, self.num_restaurants),
            'longitude': np.random.uniform(-74.0, -73.9, self.num_restaurants),
            'avg_rating': np.round(np.clip(ratings, 2.0, 5.0), 2),
            'avg_delivery_time_min': np.round(np.clip(delivery_times, 10, 50), 1),
            'is_open': np.random.choice([True, False], self.num_restaurants, p=[0.9, 0.1])
        })
    
    def generate_orders(self, customers, restaurants):
        """Generate orders with realistic demand patterns."""
        # Generate dates from 2024-01-01 to now
        start_date = datetime(2024, 9, 1)
        date_range_days = (self.date - start_date).days
        random_days = np.random.randint(0, date_range_days + 1, self.num_orders)
        order_dates = [start_date + timedelta(days=int(d)) for d in random_days]
        
        # Generate hours with demand-based weighting
        hour_weights = np.array([self._demand_at_hour(h) for h in range(24)])
        hour_weights = hour_weights / hour_weights.sum()
        hours = np.random.choice(24, self.num_orders, p=hour_weights)
        minutes = np.random.randint(0, 60, self.num_orders)
        
        order_times = [d.replace(hour=int(h), minute=int(m), second=0, microsecond=0) 
                       for d, h, m in zip(order_dates, hours, minutes)]
        
        customer_ids = np.random.choice(customers['customer_id'], self.num_orders)
        restaurant_ids = np.random.choice(restaurants['restaurant_id'], self.num_orders)
        
        order_values = np.clip(np.random.exponential(15) + 5, 5, 150)
        discounts = order_values * np.random.choice([0, 0.05, 0.10, 0.15], self.num_orders, p=[0.6, 0.2, 0.1, 0.1])
        
        statuses = np.random.choice(["completed", "cancelled"], self.num_orders, p=[0.82, 0.18])
        ratings = [int(np.random.randint(1, 6)) if s == "completed" else None for s in statuses]
        
        return pd.DataFrame({
            'order_id': [f"ORD_{uuid.uuid4().hex[:10].upper()}" for _ in range(self.num_orders)],
            'customer_id': customer_ids,
            'restaurant_id': restaurant_ids,
            'order_datetime': order_times,
            'order_value': np.round(order_values, 2),
            'discount': np.round(discounts, 2),
            'final_value': np.round(order_values - discounts, 2),
            'payment_method': np.random.choice(["card", "wallet", "cash"], self.num_orders),
            'status': statuses,
            'rating': ratings
        })
    
    def generate_deliveries(self, orders):
        """Generate deliveries for completed orders."""
        completed = orders[orders['status'] == 'completed'].copy()
        
        delivery_times = np.random.uniform(15, 45, len(completed))
        
        return pd.DataFrame({
            'delivery_id': [f"DEL_{uuid.uuid4().hex[:10].upper()}" for _ in range(len(completed))],
            'order_id': completed['order_id'].values,
            'driver_id': [f"DRV_{uuid.uuid4().hex[:7].upper()}" for _ in range(len(completed))],
            'delivery_time_min': np.round(delivery_times, 2),
            'distance_km': np.round(np.random.uniform(1, 15, len(completed)), 2),
            'rating': np.random.randint(1, 6, len(completed))
        })
    
    def generate_all(self):
        """Generate all datasets and return dataframes."""
        customers = self.generate_customers()
        restaurants = self.generate_restaurants()
        orders = self.generate_orders(customers, restaurants)
        deliveries = self.generate_deliveries(orders)
        
        return customers, restaurants, orders, deliveries
