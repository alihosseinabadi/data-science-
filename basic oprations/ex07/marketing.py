import sys

def get_sets():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    
    return set(clients), set(participants), set(recipients)

def call_center(clients, recipients):
    """Clients who haven't seen promotional email"""
    return list(clients - recipients)

def potential_clients(clients, participants):
    """Participants who are not clients"""
    return list(participants - clients)

def loyalty_program(clients, participants):
    """Clients who didn't participate in event"""
    return list(clients - participants)

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 marketing.py [call_center|potential_clients|loyalty_program]")
    
    task = sys.argv[1]
    clients, participants, recipients = get_sets()
    
    if task == "call_center":
        result = call_center(clients, recipients)
    elif task == "potential_clients":
        result = potential_clients(clients, participants)
    elif task == "loyalty_program":
        result = loyalty_program(clients, participants)
    else:
        raise Exception("Invalid task. Use: call_center, potential_clients, or loyalty_program")
    
    for email in result:
        print(email)
 
    with open('employee.tsv', 'w', encoding='utf-8') as tsv_file:
        for email in result:
         tsv_file.write(email)

if __name__ == '__main__':
    main()