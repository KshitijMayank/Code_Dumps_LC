select 
    i.invoice_id, 
    c.customer_name, 
    i.price, 
    count(t.user_id) contacts_cnt, 
    count(distinct e.email) trusted_contacts_cnt 
    
# Take out purchasing customers
from Invoices i
Inner join Customers c on i.user_id = c.customer_id  

# Get the purchasing customer's contact count
Left join Contacts t on t.user_id = c.customer_id 

# Get the number of acutal customers who purchased
Left join Customers e on e.email = t.contact_email

# ordering and grouping 
Group by invoice_id,customer_name,price
Order by invoice_id