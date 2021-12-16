from ...models import User, Task, Problem, Activity, Bug
from .keyboards import *


def ism(update, message):
    chat_id = update.message.chat_id
    user = User.objects.filter(telegram_id=chat_id).order_by('-id').first()
    user.first_name = update.message.text
    user.save()
    res = update.message.reply_text(text='Familyangizni kiriting')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'last_name'
    activity.save()


def last_name(update, message):
    chat_id = update.message.chat_id
    user = User.objects.filter(telegram_id=chat_id).order_by('-id').first()
    user.last_name = update.message.text
    user.save()
    res = update.message.reply_text(text='email kiriting')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'email'
    activity.save()


def email(update, callback):
    chat_id = update.message.chat_id
    user = User.objects.filter(telegram_id=chat_id).order_by('-id').first()
    user.email = update.message.text
    user.save()
    reply_markup = stack_keyboard()
    res = callback.bot.send_message(chat_id=chat_id, text='ish sohangizni tanlang!', reply_markup=reply_markup)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'stack'
    activity.save()


def stack(update, message):
    chat_id = update.message.chat_id
    user = User.objects.filter(telegram_id=chat_id).order_by('-id').first()
    user.stack = update.message.text
    user.save()
    res = update.message.reply_text(text='nomer kiriting \'901234567\'')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'phone_number'
    activity.save()


def phone_number(update, message):
    phone_number = update.message.text
    chat_id = update.message.chat_id
    user = User.objects.filter(telegram_id=chat_id).order_by('-id').first()
    user.phone_number = update.message.text
    user.save()
    reply_markup = tasks_keyboard()
    res = update.message.reply_text(text='Tabriklayman siz ruyxatdan utdingiz!', reply_markup=reply_markup)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


##############################################


def text_task(update, message):

    chat_id = update.message.chat_id
    Task.objects.create(user_id=User.objects.filter(telegram_id=chat_id).first(), title='title')
    user = Task.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.text = update.message.text
    user.save()
    res = update.message.reply_text(text='Ishning nomi')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'title'
    activity.save()


def title(update, message):
    chat_id = update.message.chat_id
    user = Task.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.title = update.message.text
    user.save()
    res = update.message.reply_text(text='Ishni kiriting')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'description'
    activity.save()


def description(update, message):
    chat_id = update.message.chat_id
    user = Task.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.description = update.message.text
    user.save()
    res = update.message.reply_text(text='ishni qaysi sanada yakunlaysiz\'2020-12-31\'')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'deadline'
    activity.save()


def deadline(update, message):
    chat_id = update.message.chat_id
    user = Task.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.deadline = update.message.text
    user.save()
    res = update.message.reply_text(text='statusini tanlang', reply_markup=status_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'status'
    activity.save()


def status(update, message):
    chat_id = update.message.chat_id
    user = Task.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.status = update.message.text
    user.save()
    res = update.message.reply_text(text='ishlar ruyxatiga qushildi!', reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()

############ PROBLEMS #########

def text_problem(update, message):
    chat_id = update.message.chat_id
    user = Problem.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.text = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni nomi')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'title_problem'
    activity.save()


def title_problem(update, message):
    chat_id = update.message.chat_id
    user = Problem.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.title = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni kiriting')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'description_problem'
    activity.save()


def description_problem(update, message):
    chat_id = update.message.chat_id
    user = Problem.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.description = update.message.text
    user.save()
    res = update.message.reply_text(text='muommoni darajasi', reply_markup=problem_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'type_problem'
    activity.save()


def type_problem(update, message):
    chat_id = update.message.chat_id
    user = Problem.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.type = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni bartaraf etamiz', reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()

############ BUG

def text_bug(update, message):
    chat_id = update.message.chat_id
    user = Bug.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.text = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni nomi')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'title_bug'
    activity.save()


def title_bug(update, message):
    chat_id = update.message.chat_id
    user = Bug.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.title = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni kiriting')
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'description_bug'
    activity.save()


def description_bug(update, message):
    chat_id = update.message.chat_id
    user = Bug.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.description = update.message.text
    user.save()
    res = update.message.reply_text(text='muommoni darajasi', reply_markup=problem_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'priority_bug'
    activity.save()


def priority_bug(update, message):
    chat_id = update.message.chat_id
    user = Bug.objects.filter(user_id=User.objects.filter(telegram_id=chat_id).first()).order_by('-id').first()
    user.type = update.message.text
    user.save()
    res = update.message.reply_text(text='muammoni bartaraf etamiz', reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


####### HISTORY #################

def history(update, message):
    chat_id = update.message.chat_id
    res = update.message.reply_text(text='qaysi turdagi malumotlar', reply_markup=search_button())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = 'history'
    activity.save()


# def tasks_history(update, message):
#     chat_id = update.message.chat_id
#     res = update.message.reply_text(text='malumotlarni qidiring', reply_markup=search_button())
#     activity = Activity.objects.filter(chat_id=chat_id).first()
#     activity.type = 'tasks_history'
#     activity.save()


# def problems_history(update, message):
#     chat_id = update.message.chat_id
#     res = update.message.reply_text(text='malumotlarni qidiring', reply_markup=search_button())
#     activity = Activity.objects.filter(chat_id=chat_id).first()
#     activity.type = 'problems_history'
#     activity.save()

############## tasks history

def task_history_keyboard(update, callback):
    query = update.callback_query
    print(query)
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    user = Task.objects.filter(user_id=User.objects.filter(username=chat_id).first())
    res = callback.bot.send_message(text='ishlar ruyxati', reply_markup=task_problems_keyboard(user), chat_id=chat_id)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


def task_id(update, callback, user):
    chat_id = update.callback_query.message.chat_id
    res = callback.bot.send_message(chat_id=chat_id, text=f'Title: {user.title} ' + '\n' + f'Description: {user.description}'+ '\n' + f'Status: {user.status}', reply_markup=completed_keyboard(user))
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = f'{user.id}'
    activity.save()


def not_completed_to_completed(update, callback, user):
    chat_id = update.callback_query.message.chat_id
    user.completed = 'completed'
    user.save()
    res = callback.bot.send_message(chat_id=chat_id,
                                    text='Ish bajarilganlar ruyxatiga qushildi',
                                    reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


########## problems history

def problem_history_keyboard(update, callback):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    user = Problem.objects.filter(user_id=User.objects.filter(username=chat_id).first())
    res = callback.bot.send_message(text='ishlar ruyxati', reply_markup=problems_problems_keyboard(user), chat_id=chat_id)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


def problem_id(update, callback, user):
    chat_id = update.callback_query.message.chat_id
    res = callback.bot.send_message(chat_id=chat_id, text=f'Title: {user.title} ' + '\n' + f'Description: {user.description}'+ '\n' + f'Status: {user.type}', reply_markup=completed_keyboard(user))
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = f'{user.id}'
    activity.save()

########## BUG

def bug_history_keyboard(update, callback):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat.id
    user = Bug.objects.filter(user_id=User.objects.filter(username=chat_id).first())
    res = callback.bot.send_message(text='Xatolar ruyxati', reply_markup=bugs_problems_keyboard(user), chat_id=chat_id)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()


def bug_id(update, callback, user):
    chat_id = update.callback_query.message.chat_id
    res = callback.bot.send_message(chat_id=chat_id, text=f'Title: {user.title} ' + '\n' + f'Description: {user.description}', reply_markup=fixed_keyboard(user))
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = f'{user.id}'
    activity.save()


def not_fixed_to_fixed(update, callback, user):
    chat_id = update.callback_query.message.chat_id
    user.completed = 'fixed'
    user.save()
    res = callback.bot.send_message(chat_id=chat_id,
                                    text='Ish bajarilganlar ruyxatiga qushildi',
                                    reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()



def back(update, callback):
    chat_id = update.callback_query.message.chat_id
    res = callback.bot.send_message(chat_id=chat_id,
                                    text='bosh menu',
                                    reply_markup=tasks_keyboard())
    activity = Activity.objects.filter(chat_id=chat_id).first()
    activity.type = '1'
    activity.save()

###############

def handler(update, message):
    text = update.message.text
    chat_id = update.message.chat_id
    activity = Activity.objects.filter(chat_id=chat_id).first()
    if activity.type == 'ism':
        ism(update, message)

    elif activity.type == 'last_name':
        last_name(update, message)

    elif activity.type == 'email':
        email(update, message)

    elif activity.type == 'stack':
        stack(update, message)

    elif activity.type == 'phone_number':
        phone_number(update, message)



############################################

    if update.message.text == 'TASKS':
        activity.type = 'text'
        activity.save()

    elif update.message.text == 'PROBLEMS':
        activity.type = 'text_problem'
        activity.save()
        Problem.objects.create(user_id=User.objects.filter(username=chat_id).first())

    elif update.message.text == 'BUG':
        activity.type = 'text_bug'
        activity.save()
        Bug.objects.create(user_id=User.objects.filter(username=chat_id).first())
        # Problem.objects.update(taks_id=Task.objects.filter(user_id=User.objects.filter(username=chat_id).first()).first())

    elif update.message.text == 'HISTORY':
        history(update, message)

#################          TASKS      #############

    if activity.type == 'title':
        title(update, message)

    elif activity.type == 'text':
        text_task(update, message)

    elif activity.type == 'description':
        description(update, message)

    elif activity.type == 'deadline':
        deadline(update, message)

    elif activity.type == 'status':
        status(update, message)


############### PROBLEMS

    if activity.type == 'text_problem':
        text_problem(update, message)

    elif activity.type == 'title_problem':
        title_problem(update, message)

    elif activity.type == 'description_problem':
        description_problem(update, message)

    elif activity.type == 'type_problem':
        type_problem(update, message)

####### BUG

    if activity.type == 'text_bug':
        text_bug(update, message)
    elif activity.type == 'title_bug':
        title_bug(update, message)

    elif activity.type == 'description_bug':
        description_bug(update, message)
    elif activity.type == 'priority_bug':
        priority_bug(update, message)




###### history ##########

    # if update.message.text == 'Tasks_History':
    #     tasks_history(update, message)
    #
    # elif update.message.text == 'Problems_History':
    #     tasks_history(update, message)
