from django import forms  # Import Django's form module

# Define the chart type choices as a tuple of tuples
CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

# Define the form class
class SalesSearchForm(forms.Form):
    book_title = forms.CharField(max_length=120, label='Book Title')
    chart_type = forms.ChoiceField(choices=CHART__CHOICES, label='Chart Type')
