#!/usr/bin/env python2

from model.app import App
from model.test_user import FriendshipError
from model.app import UserCreationError


def _print_counter_and_message(number, total, message):
    total_length = len(str(abs(total)))
    formatted_string = '[{0: >%s}/{1}] {2}' % total_length
    print formatted_string.format(number, total, message)


def _find_main_user(user_id, users):
    main_user = users[-1]   # The first user created is the last return by Graph API
    if user_id is None:
        for user in users:
            if user.id == user_id:
                main_user = user
                break
    return main_user


def create_users(number_of_users):
    for i in range(1, number_of_users):
        try:
            user = app.create_test_user()
            _print_counter_and_message(i, number_of_users, 'User created with id: %s' % user.id)
        except UserCreationError, e:
            _print_counter_and_message(i, number_of_users, 'Error: Cannot create user. Reason: %s' % e)
            break


def make_friendships(start_from, user_id):
    users = app.test_users
    number_of_users = len(users)
    main_user = _find_main_user(user_id, users)

    i = start_from
    for user in users[start_from:]:
        i += 1
        try:
            user.make_friend(main_user)
            _print_counter_and_message(i, number_of_users, 'Friendship made.')
        except FriendshipError, e:
            _print_counter_and_message(i, number_of_users, 'Error: Cannot make friendship. Reason: %s' % e)
            break


import argparse

if __name__ == '__main__':
    command_choices = {'create-users': create_users, 'make-friendships': make_friendships}

    command_parser = argparse.ArgumentParser(description='Facebook test accounts manager')
    subparsers = command_parser.add_subparsers(dest='command')

    create_users_parser = subparsers.add_parser('create-users', help='Create test users for the Facebook app')
    create_users_parser.add_argument('--app-id', required=True, type=int, help='your Facebook app id')
    create_users_parser.add_argument('--app-token', required=True, type=str, help='your Facebook app token')
    create_users_parser.add_argument('--number-of-users', type=int, help='number of users to create (default: %(default)s)',
                                     default=App.MAX_TEST_USERS)

    make_friendships_parser = subparsers.add_parser('make-friendships', help='Make a user friend to all others')
    make_friendships_parser.add_argument('--user-id', type=int, help='user that will be friend with all others '
                                                                '(default: the first created user)', default=None)
    make_friendships_parser.add_argument('--app-id', required=True, type=int, help='your Facebook app id')
    make_friendships_parser.add_argument('--app-token', required=True, type=str, help='your Facebook app token')
    make_friendships_parser.add_argument('--start-from', type=int, help='Start from the nth user in the list (default: %(default)s)', default=0)

    args = command_parser.parse_args()

    app = App(args.app_id, args.app_token)
    function_kwargs = {k: v for (k, v) in args.__dict__.iteritems() if k not in ('app_id', 'app_token', 'command')}

    command_choices[args.command](**function_kwargs)
