# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def stack_keyboard():
    keyboard = [
        [KeyboardButton('backend')],
        [KeyboardButton('frontend')],
        [KeyboardButton('seo')],
        [KeyboardButton('ui_ux')],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def tasks_keyboard():
    keyboard = [
        [KeyboardButton('TASKS')],
        [KeyboardButton('PROBLEMS')],
        [KeyboardButton('BUG')],
        [KeyboardButton('HISTORY')],

    ]

    markup_tasks = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_tasks

def status_keyboard():
    keyboard = [
        [KeyboardButton('started')],
        [KeyboardButton('late_submitted')],
        [KeyboardButton('completed')],

    ]

    markup_tasks = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_tasks

def problem_keyboard():
    keyboard = [
        [KeyboardButton('critical')],
        [KeyboardButton('high')],
        [KeyboardButton('medium')],
        [KeyboardButton('low')],
    ]

    markup_problem = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_problem


def search_button():
    keyboard = [
        [InlineKeyboardButton('search_button', switch_inline_query_current_chat='')],
        [InlineKeyboardButton('tasks', callback_data='callback_tasks')],
        [InlineKeyboardButton('problem', callback_data='callback_problem')],
        [InlineKeyboardButton('bug', callback_data='callback_bug')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def history_keyboard():
    keyboard = [
        [KeyboardButton('Tasks_History')],
        [KeyboardButton('Problems_History')],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def task_problems_keyboard(user):
    keyboard = []
    for i in user:
        if i.completed == 'not_completed':
            keyboard.append([InlineKeyboardButton(f'{i.title}', callback_data='prevresultt_' + str(i.id))])

    markup_problem = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_problem

def problems_problems_keyboard(user):
    keyboard = []
    for i in user:
        if i.completed == 'not_completed':
            keyboard.append([InlineKeyboardButton(f'{i.title}', callback_data='problem_' + str(i.id))])

    markup_problem = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_problem


def bugs_problems_keyboard(user):
    keyboard = []
    for i in user:
        if i.status == 'not_fixed_bug':
            keyboard.append([InlineKeyboardButton(f'{i.title}', callback_data='bug_' + str(i.id))])

    markup_problem = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup_problem


def completed_keyboard(user):
    keyboard = [
        [InlineKeyboardButton('Completed', callback_data='completed_' + str(user.id))],
        [InlineKeyboardButton('Qaytish', callback_data='back_')],
    ]
    markup_keyboard = InlineKeyboardMarkup(keyboard)
    return markup_keyboard


def fixed_keyboard(user):
    keyboard = [
        [InlineKeyboardButton('Completed', callback_data='fixed_' + str(user.id))],
        [InlineKeyboardButton('Qaytish', callback_data='back_')],
    ]

    markup_keyboard = InlineKeyboardMarkup(keyboard)
    return markup_keyboard
