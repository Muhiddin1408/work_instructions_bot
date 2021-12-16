from aiogram import Dispatcher, types, bot, executor
import requests
from django.conf import settings
# from t.types import InlineQueryResultArticle, InputTextMessageContent, ParseMode, InlineKeyboardMarkup
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent

from .keyboards import search_button
from .massages import task_history_keyboard, task_id, not_completed_to_completed, back, problem_id, problem_history_keyboard, bug_history_keyboard, bug_id
from ...models import User, Task, Problem, Activity, Bug


def start(update, callback):
    chat_id = update.message.chat_id
    chat_username = update.message.chat.username
    telegram_user = User.objects.filter(telegram_id=chat_id).first()
    activity = Activity.objects.filter(chat_id=chat_id).first()
    if not telegram_user:
        User.objects.create(telegram_id=chat_id)

    if not activity:
        Activity.objects.create(chat_id=chat_id)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    res = update.message.reply_text(text='ismingizni kiriting')
    activity.type = 'ism'
    activity.save()


def search(update, callback):
    chat_id = update.inline_query.from_user.id
    print(chat_id)
    activity = Activity.objects.filter(chat_id=chat_id).first()
    if activity.type == 'tasks_history':
        query = update.inline_query.query
        response = Task.objects.filter(completed='completed')
        results = list()
        for result in response:
            if result.title == query:
                results.append(
                    InlineQueryResultArticle(
                        id=result.id,
                        title=result.title,
                        input_message_content=InputTextMessageContent(
                            message_text=result.title
                           )
                    ),
                )

        print(results)
        update.inline_query.answer(results)
        # bot.answerInlineQuery(update.inline_query.id, results=results, cache_time=10

    # region_id = []
    # region = user.region
    # print(region.name)
    # # region_id.append(region.id)
    # # if not region.parent:
    # #     for i in Region.objects.filter(parent=region):
    # #         region_id.append(i.id)
    # if len(query) >= 3:
    #     results = []
    #     drugs = Product.objects.filter(
    #         Q(name__startswith=query) | Q(description__icontains=query) & Q(region_order=region.name) & Q(status=True))
    #     if drugs.count() == 0:
    #         drugs = Product.objects.filter(description__icontains=query, region_order=region.name, status=True)
    #     if drugs.count()==0:
    #         results = [
    #             InlineQueryResultArticle(
    #                 id=0,
    #                 title="Bunday mahsulot yo\'q",
    #                 input_message_content=InputTextMessageContent(
    #                     escape_markdown('search_not'),
    #                     parse_mode=ParseMode.MARKDOWN)
    #             )
    #         ]
    #         update.inline_query.answer(results)
    #     else:
    #         for drug in drugs:
    #             thumb = drug.image.url
    #             desc = str(drug.price) + '\n'
    #             desc += drug.name
    #             results.append(
    #                 InlineQueryResultArticle(
    #                     id=drug.id,
    #                     title=drug.name,
    #                     # photo_url='https://s.daryo.uz/wp-content/uploads/2021/05/Toshkent-b-Daryo.jpg',
    #                     thumb_url=f'http://saxro.uz/{drug.image.url}',
    #                     description=desc,
    #                     input_message_content=InputTextMessageContent(
    #                         'a'+str(drug.id),
    #                         parse_mode=ParseMode.MARKDOWN),
    #                 ),
    #
    #             )
    # else:
    #     results = [
    #         InlineQueryResultArticle(
    #             id=0,
    #             title="Endi kamida 3 ta belgidan iborat e'lon nomini kiriting.",
    #             input_message_content=InputTextMessageContent(
    #                 escape_markdown('search_drug'),
    #                 parse_mode=ParseMode.MARKDOWN)
    #         )
    #     ]
    #
    # update.inline_query.answer(results)


def callback_tasks(update, callback):
    query = update.callback_query
    query.answer()
    drug = query.data.split('_')[1]
    if 'callback_tasks' in query.data:
        task_history_keyboard(update, callback)
    elif 'prevresultt_' in query.data:

        user = Task.objects.filter(id=drug).first()
        task_id(update, callback, user)
    elif 'completed_' in query.data:
        user = Task.objects.filter(id=drug).first()
        not_completed_to_completed(update, callback, user)

    elif 'callback_problem' in query.data:
        problem_history_keyboard(update, callback)

    elif 'problem_' in query.data:
        problem = Problem.objects.filter(id=drug).first()
        problem_id(update, callback, problem)

    elif 'callback_bug' in query.data:
        bug_history_keyboard(update, callback)
    elif 'bug_' in query.data:
        bug = Bug.objects.filter(id=drug).first()
        bug_id(update, callback, bug)
    elif 'fixed_' in query.data:
        user = Bug.objects.filter(id=drug).first()
        not_completed_to_completed(update, callback, user)

    elif 'back_' in query.data:
        back(update, callback)


if __name__ == '__main__':
    executor.start_polling()