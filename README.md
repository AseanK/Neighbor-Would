<img align="right" width="33%" height="33%" src="/static/image/logo.png">

# Neighbor-Would
[NeighborWould](https://neighborwould-9c76a564d773.herokuapp.com) is a website designed to connect neighbors and keep them informed about local events. Never miss out on garage sales, fairs, parties, and more in your community!

## 🌌 Inspiration
It is built for Hackspree 1.0 hackathon.

**Have you ever missed out on local events simply because you weren't aware they were taking place?**

Well, unfortunately, I found myself in the same position. NeighborWould is my solution to this problem!

## 🤔 What it does

NeighborWould is a website that aims to connect neighbors together by allowing them to post and discover a wide range of local events, including garage sales, fairs, markets, parties, and more. Additionally, it allows users to share important notices, such as road construction updates. One of the key features of NeighborWould is the event calendar.

##  🚀 How we built it

NeighborWould is mainly built with Python, JavaScript, HTML, CSS, and SQL. NeighborWould uses a variety of frameworks and tools for its various features.

- **Flask**: A lightweight web framework for Python.
- **Jinja**: A web template engine for Python.
- **Gunicorn**: Python Web Server Gateway Interface HTTP server.
- **Bootstrap**: CSS framework for styling.
- **SQLAlchemy**: SQL toolkit and object-relational mapper for Python.
    - Used to interact with the database.
- **PostgreSQL**: Relational database management system emphasizing extensibility and SQL compliance.
    - Used to manage and store database.
- **FullCalendar**: React calendar component that accepts JSX for rendering nested content.
    - Used to render the calendar.
- **Mapbox**: Used to request and render maps and addresses.
- **Heroku**: A cloud PAAS (platform as a service) supporting several programming languages.
    - Used to deploy/host the website.

## 🔍 Challenges we ran into

During the development process, I encountered various challenges, one of them being integrating fullcalendar and mapbox with the backend, it took some effort to ensure the JavaScript files worked seamlessly with the database managed by SQLAlchemy and Flask. I utilized online resources (google and Stack Overflow), and read documentation for the frameworks countless times to find the best solution. Another is the style of the website. I searched and studied a lot of front-end (UI/UX) and was able to accomplish the NeighborWould as it is now. 

## ✨ Accomplishments that we're proud of

I paid special attention to the front-end design, focusing on creating an approachable and user-friendly interface. To achieve this, I chose a green theme to give the website a friendly and inviting look. I'm also proud of creating a useful website that is both technical and visually appealing for individuals to use.

## 💡 What we learned

I learned to use various frameworks and utilize different frameworks with different programming languages. I gained valuable insights into integrating several features into a single website. I also learned a lot about the front-end development.

## 📌 What's next for Neighbor-Would

- I'm unsure if I want to add the login features to the website since I want users to feel as friendly as possible. I asked a few of my friends about their opinions and most of them didn't want to bother registering and login to post an event. Maybe in the future, I might consider it again but for now, I'm happy with how it turned out.

- The mobile version of the website isn't as visually appealing as the PC version. Though, it is supported. I will work on that in the future.
