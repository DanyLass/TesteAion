from datetime import datetime

from product_db import product_db
from sale_order_db import sale_order_db

def get_kpis(selected_date_from, selected_date_to):
	selected_date_from = datetime.strptime(selected_date_from, '%Y-%m-%d')
	selected_date_to = datetime.strptime(selected_date_to, '%Y-%m-%d')

	total_revenue = 0
	total_canceled = 0
	total_sales_qty = len(sale_order_db) 
	
	for sales_list in sale_order_db: 
		sale_date = sales_list['sale_order_purchased_at']
		filtered_date = (sale_date <= selected_date_from) and (sale_date >= selected_date_to)
		if(filtered_date):
			for purchased_products in sales_list['purchased_products']:
				for products_list in product_db:
					if purchased_products == products_list['product_id']:
						full_price = products_list.get('full_price')
						total_revenue = total_revenue + full_price			
		else:
			for purchased_products in sales_list['purchased_products']:
				is_canceled = sales_list.get('is_canceled')
				if(is_canceled) is True:
					canceled_sales_qty = len(sales_list['purchased_products'])
					for products_list in product_db:
						if purchased_products == products_list['product_id']:
							total_canceled = canceled_sales_qty / total_sales_qty 		


	kpis = {
		'total_revenue': total_revenue,
	 	 'cancellation': total_canceled 
	}

	return kpis

kpis = get_kpis('2021-07-01', '2021-06-08')
print(kpis)

