"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("name", validators=[InputRequired(message="Please enter the name")])

    description = TextAreaField("description", validators=[
                       InputRequired(message="Description can't be blank")])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title= StringField("title", validators=[InputRequired(message="Title cannot be blank")])
    artist= StringField("artist", validators=[InputRequired(message="Artist cannot be blank")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
