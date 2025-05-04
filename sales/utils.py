from books.models import Book
from io import BytesIO
import base64
import matplotlib.pyplot as plt



# Function to get book name from ID
def get_bookname_from_id(val):
    book = Book.objects.get(id=val)
    return book.name


# Generates a base64-encoded graph from current matplotlib figure
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# Builds chart based on user input and DataFrame data
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':  # Bar chart
        plt.bar(data['date_created'], data['quantity'])
    elif chart_type == '#2':  # Pie chart
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels)
    elif chart_type == '#3':  # Line chart
        plt.plot(data['date_created'], data['price'])
    else:
        print('Unknown chart type')

    plt.tight_layout()
    chart = get_graph()
    return chart
