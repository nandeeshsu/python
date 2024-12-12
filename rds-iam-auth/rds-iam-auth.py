import boto3
import psycopg2
from psycopg2 import sql

def generate_rds_auth_token(region, host, port, username):
    """
    Generate an IAM authentication token for AWS RDS PostgreSQL.
    """
    client = boto3.client('rds', region_name=region)
    auth_token = client.generate_db_auth_token(
        DBHostname=host,
        Port=port,
        DBUsername=username
    )
    return auth_token

def connect_to_rds_postgresql(region, host, port, username, dbname):
    """
    Connect to AWS RDS PostgreSQL using IAM authentication.
    """
    # Generate the authentication token
    auth_token = generate_rds_auth_token(region, host, port, username)

    try:
        # Establish the connection
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=auth_token,
            dbname=dbname,
            sslmode='require'
        )
        print("Connection successful!")
        return connection
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return None

# Example usage
if __name__ == "__main__":
    REGION = "us-east-1"  # Replace with your RDS instance region
    HOST = "your-rds-endpoint.rds.amazonaws.com"  # Replace with your RDS endpoint
    PORT = 5432  # Default PostgreSQL port
    USERNAME = "your-username"  # Replace with your database username
    DBNAME = "your-database"  # Replace with your database name

    connection = connect_to_rds_postgresql(REGION, HOST, PORT, USERNAME, DBNAME)
    if connection:
        # Perform database operations
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        print("PostgreSQL version:", cursor.fetchone())
        cursor.close()
        connection.close()
