from django_tables2 import tables, columns
from django_tables2.utils import A
from demo.models import Person

class PersonTable(tables.Table):
    id = columns.LinkColumn('demo-person-detail',
                            text=lambda o: o.id,
                            args=[A('id')])
    created_date = columns.DateTimeColumn(format='Y-m-d H:i')
    modified_date = columns.DateTimeColumn(format='Y-m-d H:i')

    full_name = tables.Column(
         accessor="get_full_name", # This would call record.get_full_name()
         verbose_name="Full Name",
         order_by=("firstname", "lastname")
    )

    delete = columns.LinkColumn(
        'demo-person-delete',
        args=[A('pk')],
        text='Delete',  # Optional: Text to display in the link
        attrs={'class': 'delete-link'})  # Optional: Add HTML attributes to the link

    class Meta:
        model = Person
        sequence = ('id', 'full_name', 'firstname', 'lastname', 'comment', 'username',
                    'created_date', 'modified_date', 'email', 'delete')
        exclude = ('website', 'salary', 'is_active', 'weight', 'height', 'is_deleted')
