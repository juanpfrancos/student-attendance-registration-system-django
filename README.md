# Student Attendance Registration System


## Description

This web application developed in Django allows users to efficiently track student attendance in an educational setting. Users can easily mark students' attendance using checkboxes and submit the data with a single click. The application then provides a convenient way to view who attended on a specific date.

## Stack

- Python with Django.
- SQLite.
- Puppertino CSS.

## Features

- Add students with detailed information.
- Record student attendance by selecting checkboxes and submitting the data.
- View the list of students who attended on a given date.
- User-friendly interface for attendance tracking.


## Installation

Below are the steps to install and run the application in your local environment.

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/juanpfrancos/student-attendance-registration-system-django.git
   ```

2. Navigate to the project directory:

   ```
   cd student-attendance-registration-system-django
   ```

3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin panel (if needed):

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Open your web browser and access the application at `http://localhost:8000`.

## Usage

1. Add students.
3. Select the date for which you want to record attendance.
4. Mark the checkboxes for students who attended.
5. Click the "Submit" button to record attendance.
6. View the list of students who attended on a specific date in the "Reports" section of the application.

## Contribution

If you wish to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution: `git checkout -b feature/new-feature`.
3. Make your changes and ensure that tests pass.
4. Commit your changes: `git commit -m "Add new feature"`.
5. Push to your branch: `git push origin feature/new-feature`.
6. Create a pull request on GitHub.

## License

This project is under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- Email: juanpfrancos@programmer.net
- GitHub: [yourusername](https://github.com/juanpfrancos)

---
