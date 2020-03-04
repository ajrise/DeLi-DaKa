from django import forms

class reg_form(forms.Form):
    <label for= "you name">Your name :</label>
    <input id="you_name" type="text" name = "your_name" value="{{current_name}}">