# Uber Data Project
[Click here for full data set information][def]

### About the Dataset
**Uber Ride Analytics Dataset 2024**

This comprehensive dataset contains detailed ride-sharing data from Uber operations for the year 2024, providing rich insights into booking patterns, vehicle performance, revenue streams, cancellation behaviors, and customer satisfaction metrics.

## Dataset Overview

The dataset captures 148,770 total bookings across multiple vehicle types and provides a complete view of ride-sharing operations including successful rides, cancellations, customer behaviors, and financial metrics.

### Key Statistics:

- Total Bookings: 148.77K rides

- Success Rate: 65.96% (93K completed rides)

- Cancellation Rate: 25% (37.43K cancelled bookings)
Customer 

- Cancellations: 19.15% (27K rides)

- Driver Cancellations: 7.45% (10.5K rides)

### Data Schema

The dataset contains the following columns:

| Column Name  | Description |
|---|---|
| Date |Date of the booking|
| Time | Time of the booking |
| Booking ID | Unique identifier for each ride booking |
| Booking Status | Status of booking (Completed, Cancelled by Customer, Cancelled by Driver, etc.)|
| Customer ID | Unique identifier for customers |
| Vehicle Type | Type of vehicle (Go Mini, Go Sedan, Auto, eBike/Bike, UberXL, Premier Sedan) |
| Pickup Location | Starting location of the ride |
| Drop Location | Destination location of the ride |
| AVG VTAT | Average time for driver to reach pickup location (in minutes) |
| AVG CTAT |Average trip duration from pickup to destination (in minutes) |
| Cancelled Rides by Customer | Customer-initiated cancellation flag |
| Reason for cancelling by customer | Reason for customer cancellation |
| Cancelled Rides by Driver | Driver-initiated cancellation flag |
| Driver Cancellation Reason | Reason for driver cancellation |
| Incomplete Rides	 | Incomplete ride flag |
| Incomplete Rides Reason | Reason for incomplete rides |
| Booking Value | Total fare amount for the ride |
| Ride Distance | Distance covered during the ride (in km) |
| Driver Ratings | Rating given to driver (1-5 scale) |
| Customer Rating |Rating given by customer Method used for payment (UPI, Cash, Credit Card, Uber Wallet, Debit Card)|


### Vehicle Fleet Coverage

| Vehicle Type | Total Bookings	|Success Rate |	Avg Distance | Total Distance |
|---|---|---|---|---|
Auto |	12.88M	| 91.1%	| 25.99 km	| 602K km|
eBike/Bike |	11.46M	| 91.1%	 | 26.11 km |	537K km |
Go Mini	| 10.34M	| 91.0%	| 25.99 km | 	482K km
Go Sedan |	9.37M |	91.1% |	25.98 km |	433K km
Premier Sedan |	6.28M |	91.2% |	25.95 km |	292K km |
UberXL |	1.53M	| 92.2%	| 25.72 km |	72K km |

### Revenue Distribution by Payment Method

- UPI: Highest contributor (~40% of total revenue)
- Cash: Second highest (~25% of total revenue)
- Credit Card: ~15% of total revenue
- Uber Wallet: ~12% of total revenue
- Debit Card: ~8% of total revenue

### Cancellation Patterns

**Customer Cancellation Reasons**:

- Wrong Address: 22.5%
- Driver Issues: 22.4%
- Driver Not Moving: 22.2%
- Change of Plans: 21.9%
- App Issues: 11.0%
- Driver Cancellation Reasons:
- Capacity Issues: 25.0%
- Customer Related Issues: 25.3%
- Personal & Car Issues: 24.9%
- Customer Behavior: 24.8%

### Rating Analysis
- Customer Ratings: Consistently high across all vehicle types (4.40-4.41)
- Driver Ratings: Slightly lower but stable (4.23-4.24)
- Highest Rated: Go Sedan (4.41 customer rating)
- Most Satisfied Drivers: UberXL category (4.24 rating)

### Data Quality
- Completeness: Comprehensive coverage with minimal missing values
- Consistency: Standardized vehicle types and status categories
- Temporal Coverage: Full year 2024 data with daily granularity
- Geographic Scope: Multiple pickup and drop locations
- Balanced Distribution: Good representation across all vehicle types and time periods.

[def]: https://public.tableau.com/views/StormDashboard_17559311714590/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
