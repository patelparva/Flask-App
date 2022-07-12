from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[{'id':1,'Name':'Harshil','Contact':9924742690,'done':False},
        {'id':2,'Name':'Parva','Contact':9904460969,'done':False}]

@app.route('/')
def greetings():
    return 'Thank you for visiting this website.\nTo view the contacts type \'get_contacts\' after the above link.'

@app.route('/add_contacts',methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the Contacts!'
        },400)
    
    contact={'id':contacts[-1]['id']+1,'Name':request.json['Name'],'Contact':request.json['Contact'],'done':False}
    contacts.append(contact)

    return jsonify({
        'status':'Success',
        'message':'Contact Added Successfully'
    },200)

@app.route('/get_contacts')
def get_data():
    return jsonify({'data':contacts})

if __name__=='__main__':
    app.run(debug=True)