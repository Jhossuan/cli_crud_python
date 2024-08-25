import json_manager
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='User name:')
@click.option('--lastname', required=True, help='User last name:')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        return ctx.fail('name and lastname are required *')
    else:
        data = json_manager.read_json()
        data.reverse()
        new_id = None
        if len(data) == 0:
            new_id = 0
        else:
            new_id = data[0]['id'] + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} saved correctly")

@cli.command()
def users():
    userdata = json_manager.read_json()
    if len(userdata) == 0:
        return print('There are no users')
    for user in userdata:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((i for i in data if i['id'] == id), None)
    if user is None:
        print("This user not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def delete(id):
    isok = click.prompt('Are you sure? yes/no')
    if not isok:
        return print('Yes or No required')
    elif isok.lower() == 'no':
        return print('The user has not been deleted')
    data = json_manager.read_json()
    user = next((i for i in data if i['id'] == id), None)
    if user is None:
        print("This user not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User {user['id']} is deleted")

@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='User name:')
@click.option('--lastname', help='User lastname:')
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    return print(f"User {id} has been updated")

if __name__ == "__main__":
    cli()

