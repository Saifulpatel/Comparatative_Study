from flask_wtf import FlaskForm # type: ignore
from wtforms import FileField, SubmitField # type: ignore
from wtforms.validators import DataRequired # type: ignore

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[DataRequired()])
    submit = SubmitField('Generate Accuracy')
