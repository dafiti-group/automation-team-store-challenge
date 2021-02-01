import csv, io
from django.shortcuts import render
from django.contrib import messages

# one parameter named request
def read_csvfile(request):

    # declaring template
    template = "read_csvfile.html"
    data = Shoe.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be id, name, price, size, style, type, color, brand, post_date, status',
        'shoes': data
              }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['src/data.csv']

    # Checking if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = Shoe.objects.update_or_create(
            id=column[0],
            name=column[1],
            price=column[2],
            size=column[3],
            style=column[4],
            type=column[5],
            color=column[6],
            brand=colum[7],
            post_date=colum[8],
            status=colum[9]
        )
    context = {}
    return render(request, template, context)
