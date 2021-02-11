from django import forms

class Author_form(forms.Form):
    author_name = forms.CharField( max_length = 50, 
    required = True, 
    label = "Author's name", 
    help_text = "Input author's name")
    description = forms.Textarea()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("author's name")

        if name == "Taboo":
            self.add_error(name, ' This name is forbiden')

        return cleaned_data