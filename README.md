WatchWorld - Shop Watches
A Flask-based web application that allows users to browse watches, place orders, and choose between payment methods (Mpesa or Cash on Delivery). The app is deployed on PythonAnywhere and uses MongoDB Atlas for storing and managing order data.

Features
Product Listings: Displays a collection of luxury and modern watches.
Order Placement: Users can place orders by filling out a form.
Payment Options: Users can choose to pay via Mpesa or Cash on Delivery.
Admin Dashboard: Admins can view and manage orders with the option to update order statuses (Pending/Delivered).
MongoDB Atlas: Stores order information securely in a cloud database.
Technologies Used
Backend: Flask (Python Web Framework)
Database: MongoDB Atlas (Cloud Database)
Frontend: HTML, CSS (Responsive Design)
Hosting: PythonAnywhere (Deployment)
Installation
1. Clone the Repository
Clone the repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/yourusername/WatchWorld.git
2. Install Dependencies
Ensure you have pip installed, then install the required Python packages:

bash
Copy code
cd WatchWorld
pip install -r requirements.txt
3. Set Up MongoDB Atlas
Create a MongoDB Atlas account and set up a free cluster.
Create a new database and a collection (e.g., orders).
Add a database user and whitelist your IP address (or use 0.0.0.0/0 for all IPs).
Obtain your MongoDB Atlas connection string.
4. Configure MongoDB Connection
In app.py, replace the MongoDB URI with your connection string:

python
Copy code
mongo_uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
Alternatively, you can store the connection string in an environment variable for better security:

bash
Copy code
export MONGO_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
Running the Application Locally
To run the application locally, use the following command:

bash
Copy code
python app.py
Visit http://127.0.0.1:5000 in your browser to see the app in action.

Deployment on PythonAnywhere
1. Set Up a PythonAnywhere Account
Sign up at PythonAnywhere.
2. Upload Your Files
Go to the Files tab on PythonAnywhere and upload all your app files, including app.py, requirements.txt, static/, and templates/.
3. Create a Virtual Environment
Open a Bash console and create a virtual environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
4. Configure the Web App
Go to the Web tab, click Add a new web app, and select Flask.
Set up the WSGI configuration file to point to app.py (Flask app entry point):
python
Copy code
import sys
from os.path import dirname, abspath
project_home = u'/home/yourusername/WatchWorld'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path
from app import app as application
5. Reload the Web App
After uploading your files and configuring your app, click Reload in the Web tab.
6. Access Your Deployed App
Once deployed, you can access your app at:

arduino
Copy code
https://yourusername.pythonanywhere.com
Using MongoDB Atlas
Access MongoDB Atlas: MongoDB Atlas Console
Create a Cluster: Set up a cluster in MongoDB Atlas, and add your database and collection (e.g., orders).
Whitelist IP: Allow access from your IP or set 0.0.0.0/0 for all IPs.
Create a Database User: Add a user with proper credentials and give access to your database.
Admin Dashboard
Admins can view orders and update their status (Pending/Delivered).

URL: /admin/orders
Features:
View a list of all orders.
Update the order status via a dropdown (Pending/Delivered).
Future Enhancements
Authentication: Add user authentication to protect the admin dashboard.
Payment Integration: Integrate actual payment gateways (like Mpesa or PayPal).
Admin Analytics: Add analytics for the admin to view orders, payments, and more.
Contributing
Fork the repository.
Create a new branch for your feature.
Commit changes and push them to your branch.
Open a pull request with a description of your changes.
License
This project is open-source and available under the MIT License.

Contact
For any inquiries or support, please contact us at:

Email: support@watchworld.com
Acknowledgements
Flask for the web framework.
MongoDB Atlas for cloud database management.
PythonAnywhere for web app hosting.
