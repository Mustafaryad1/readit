from django import forms
from .models import Book


class ReviewForm(forms.Form):
    """
    Form for Reviewing a book
    """

    is_favorite = forms.BooleanField(
        label='Favorite?',
        help_text='In your top 100 books of all your time?',
        required=False
    )

    review = forms.CharField(
        widget=forms.Textarea,
        min_length=300,
        error_messages={
            'required': 'please enter your review',
            'min_length': 'please write at least 300 chars (you have written %(show_value)s)'
        }
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors','reviewed_by']

    def clean(self):
        # edit super method
        super(BookForm, self).clean()
        try:
            title = self.cleaned_data.get('title')
            authors = self.cleaned_data.get('authors')
            book = Book.objects.get(title=title, authors=authors)

            raise forms.ValidationError(
                'The book {} by  {} already exist'.format(title, book.list_author()),
                code='bookexists')
        except Book.DoesNotExist:
            return  self.cleaned_data
