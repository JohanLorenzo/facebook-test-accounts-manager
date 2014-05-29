#!/usr/bin/env python2

from model.app import App
from model.test_user import FriendshipError
from model.app import UserCreationError


def _print_counter_and_message(number, total, message):
    total_length = len(str(abs(total)))
    formatted_string = '[{0: >%s}/{1}] {2}' % total_length
    print formatted_string.format(number, total, message)


def create_users(number_of_users):
    for i in range(1, number_of_users):
        try:
            user = app.create_test_user()
            _print_counter_and_message(i, number_of_users, 'User created with id: %s' % user.id)
        except UserCreationError, e:
            _print_counter_and_message(i, number_of_users, 'Error: Cannot create user. Reason: %s' % e)
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

    args = command_parser.parse_args()

    app = App(args.app_id, args.app_token)
    function_kwargs = {k: v for (k, v) in args.__dict__.iteritems() if k not in ('app_id', 'app_token', 'command')}

    command_choices[args.command](**function_kwargs)
