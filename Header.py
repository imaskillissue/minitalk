import datetime
import getpass
import os


def generate_header(filename, user, email):
    useremail = f"{user} <{email}>"
    header = f"""/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   {filename:51}:+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: {useremail:37}      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: {datetime.datetime.now():%Y/%m/%d %H:%M:%S} by {user:12}      #+#    #+#             */
/*   Updated: {datetime.datetime.now():%Y/%m/%d %H:%M:%S} by {user:12}     ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
"""
    return header

def add_header_to_file(filename, header):
    # Open the file in read mode and store its contents
    with open(filename, 'r') as file:
        original_contents = file.read()

    # Open the file in write mode, write the header and the original contents
    with open(filename, 'w') as file:
        file.write(header + '\n' + original_contents)

user = getpass.getuser()
email = os.getenv('EMAIL', 'ekarpawi@student.42.fr')

# For each file in the current directory that ends with .c or .h
for filename in os.listdir('.'):
    if filename.endswith('.c') or filename.endswith('.h'):
        header = generate_header(filename, user, email)
        add_header_to_file(filename, header)
