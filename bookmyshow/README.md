# LLD of Book my show(without LLD knowledge)

# Requirements gathering

- You can see the list of theatres.
- You can see all available movies
- Select confirm the seats.
- Theatre can have multiple auditoriums.
- Add/modify/delete the show/movie.
- Add/modify the theatre.

Entities:
User -> Customer
-> Admin

Customer:

- id
- username
- email
- password
- name(first name and last name)

Movie/show:

- id
- name
- language
- info

Rating

- id
- rating value
- movie_id
- description

Theatre:

- id
- name
- Location

Seat:

- id
- audi_id
- Name
- user_id(one to one relationship)

Auditorium:

- id
- name
- theatre_id
- seat_capacity

Auditorium_movie(many to many):

- id
- movie_id
- audi_id

Ticket

- id
- movie_id
- user_id(one2one)
- booking_id

Booking

- id
- is_active
- user_id
- cost

Timeslot

- id
- timestamp

timeslot_movie_theatre(many to many)

- id
- movie_id
- timeslot_id
- theatre_id

Flow:

- user logs in --> /api/login
- they can check different movies --> /api/movies
- movie detail --> /api/movies/<id>
  --> all the theatres in which the movie is playing
  --> all the timeslots available in those theatres
- booking page ==> /api/booking/new
- admin --> can add/delete/modify movies, theatres
  --> can block/delete users
