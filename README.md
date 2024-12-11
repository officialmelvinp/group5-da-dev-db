```markdown
# IMF Data Analysis Project

This project is a Django-based application for managing and analyzing IMF (International Monetary Fund) data. It provides models for storing country information, annual data, and quarterly data.

## Project Setup

1. Clone the repository:
```

git clone [https://github.com/officialmelvinp/group5-da-dev-db.git](https://github.com/officialmelvinp/group5-da-dev-db.git)
cd group5-da-dev-db

```plaintext

2. Create a virtual environment and activate it:
```

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```plaintext

3. Install the required packages:
```

pip install -r requirements.txt

```plaintext

4. Copy the `.env.example` file to `.env` and update the values:
```

cp .env.example .env

```plaintext

5. Update the `.env` file with your database credentials and other configuration.

## Database Schema

The project consists of three main models:

1. **Country**
- `country_id` (AutoField, primary key)
- `country` (CharField, unique)

2. **AnnualData**
- `annual_id` (AutoField, primary key)
- `country` (ForeignKey to Country)
- `metric` (CharField)
- `year` (IntegerField)
- `value` (DecimalField)

3. **QuarterlyData**
- `quarter_id` (AutoField, primary key)
- `country` (ForeignKey to Country)
- `metric` (CharField)
- `year` (IntegerField)
- `quarter` (CharField)
- `value` (DecimalField)

## Running Migrations

To set up your database schema, run the following commands:

```

python manage.py makemigrations
python manage.py migrate

```plaintext

## Loading Initial Data

Sample CSV files are provided in the `data/` directory. To load this data into your database, use the custom management command:

```

python manage.py load_data

```plaintext

This command will populate your database with the data from:
- `data/countries.csv`
- `data/annual_data.csv`
- `data/quarterly_data.csv`

## Environment Variables

Ensure the following environment variables are set in your `.env` file:

- `DEBUG`: Set to `True` for development, `False` for production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: URL for your database connection

Example:
```

DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://user:password@localhost/dbname

```plaintext

## API Endpoints

If you need programmatic access to the data, the following API endpoints are available:

- `/api/countries/`: List and create countries
- `/api/annual-data/`: List and create annual data
- `/api/quarterly-data/`: List and create quarterly data

## Running the Project

To run the development server:

```

python manage.py runserver

```plaintext

The server will start at `http://127.0.0.1:8000/`.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for det
```