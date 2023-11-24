def visitors():

	counter_read_file = open("Count.txt", "r")
	visitors_counts = int(counter_read_file.read())
	counter_read_file.close()


	visitors_counts = visitors_counts + 1


	counter_write_file = open("Count.txt", "w")
	counter_write_file.write(str(visitors_counts))
	counter_write_file.close()

	print('Total visitors : ', visitors_counts)

visitors()



def covid_stats():

	country_code = input('Enter country Name: ')

	corona_data = '' + country_code
	print(corona_data)


covid_stats()