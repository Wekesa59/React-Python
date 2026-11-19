from flask import request, jsonify
from Config.config import app, db
from Model.models import Contact

#Grab contacts from db and convert to useable json
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

#Creating a contact
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    checking_account = request.json.get("checkingAccount")
    savings_account = request.json.get("savingsAccount")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name and email"}), 400
    if not checking_account or not savings_account:
        return jsonify({"message": "You must include a checking account and savings account"}), 400

    new_contact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        checking_account=checking_account,
        savings_account=savings_account
    )

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created successfully"}), 201

#Updating a contact
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    contact.checking_account = data.get("checkingAccount", contact.checking_account)
    contact.savings_account = data.get("savingsAccount", contact.savings_account)

    db.session.commit()
    return jsonify({"message": "User updated!"}), 200

#Deleting a contact
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    # If db does not exist, create it
    with app.app_context():
        db.create_all()

    app.run(debug=True)