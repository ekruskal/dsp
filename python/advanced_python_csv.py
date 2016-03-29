def write_data(data):
    with open('emails.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in data:
            writer.writerow([i])
    return 'emails.csv'
write_data(email_addresses)
