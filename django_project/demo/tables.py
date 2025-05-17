from django_tables2 import tables, columns
from django_tables2.utils import A
from demo.models import Person

class PersonTable(tables.Table):
    id = columns.LinkColumn('demo-person-detail',
                            text=lambda o: o.id,
                            args=[A('id')])
    created_date = columns.DateTimeColumn(format='Y-m-d H:i')
    modified_date = columns.DateTimeColumn(format='Y-m-d H:i')

    delete = columns.LinkColumn(
        'demo-person-delete',
        args=[A('pk')],
        text='Delete',  # Optional: Text to display in the link
        attrs={'class': 'delete-link'})  # Optional: Add HTML attributes to the link

    class Meta:
        model = Person
