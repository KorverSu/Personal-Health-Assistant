import json
import math
import os
import random
import string
import tempfile
from typing import List

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage, VideoSendMessage, ImagemapSendMessage
from linebot.models import FlexSendMessage

from .GMeet import *
from .classPkg.Contact import Contact
from .classPkg.Order import Order
from .classPkg.Reservation import Reservation
from .classPkg.Times import Times
from .ka import get_select, produce, check_counter, kaf
from .classPkg.Choice import Choice
from .classPkg.Entry import *
from .classPkg.Topic import *
from .classPkg.Choice import *
from .classPkg.Result import *
from .classPkg.User import *
from .classPkg.Vote import *
from .classPkg.Menu import *
from .classPkg.Measurement import *
from .classPkg.Pose import *
from .classPkg.Carousel import *
from .classPkg.Comment import *
from .classPkg.Return import *
from .classPkg.Lists import *
from .classPkg.Dao import *
import requests
import pyimgur

from moviepy.editor import *
from .demoJson import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)



@csrf_exempt
def callback(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        events = parser.parse(body, signature)  # 傳入的事件
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()

    def message_type_condition(alt: str, contents: list or dict):
        output_flex_message: dict = {}
        if type(contents) == list:
            output_flex_message = {
                "type": "carousel",
                "contents": [*contents]
            }
        else:
            output_flex_message = {**contents}

        return FlexSendMessage(
            alt_text=alt,
            contents=output_flex_message,
        )

    def get_userID():
        dic = json.loads(str(event.source))
        user_id = dic['userId']
        return user_id

    def call_bubble_or_carousel(interface_json):  # 呼叫bubble
        try:
            con = message_type_condition('newMessage', interface_json)
            line_bot_api.reply_message(event.reply_token, con)
        except Exception:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage('json error')
            )

    def uploadMp4(directory='/usr/local/forTest/photo/123.mp4'):
        url = "https://api.imgur.com/3/upload"

        payload = {'album': 'ALBUMID',
                   'type': 'file',
                   'disable_audio': '0'}
        files = [
            ('video', open(directory, 'rb'))
        ]
        headers = {
            'Authorization': 'Bearer BEARERTOKENHERE'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text.encode('utf8'))
        link = response.text.encode('utf8')
        return link

    for event in events:
        if not isinstance(event, MessageEvent):  # 如果有訊息事件
            return HttpResponse()

        lineID = get_userID()
        dao = Dao(lineID)

        msg = None
        ###
        if event.message.type == 'text':
            msg = event.message.text
        elif event.message.type == 'image':
            msg = 'isjpg'
        elif event.message.type == 'video':
            msg = 'ismp4'
        print(event.source)
        ###
        '''
        #讀mp4
        message_content = line_bot_api.get_message_content(msg)
        with tempfile.NamedTemporaryFile(dir='/usr/local/forTest/photo', prefix='mp4', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name

        print(tempfile_path)
        dist_path = tempfile_path + '.' + 'mp4'
        dist_name = os.path.basename(dist_path)
        os.rename(tempfile_path, dist_path)  # dist_path is mp4 directory

        clip = (VideoFileClip(dist_path))
        newGif = dist_name + ".gif"
        clip.write_gif(newGif)
        print("Conversion completed")

        link = uploadMp4(dist_path)
        link = json.loads(link)
        '''

        '''image = tf.io.read_file('/usr/local/forTest/photo/' + newGif)
        image = tf.image.decode_gif(image)

        # Load the input image.
        num_frames, image_height, image_width, _ = image.shape
        crop_region = init_crop_region(image_height, image_width)

        output_images = []
        bar = display(progress(0, num_frames - 1), display_id=True)
        for frame_idx in range(num_frames):
            keypoints_with_scores = run_inference(
                movenet, image[frame_idx, :, :, :], crop_region,
                crop_size=[input_size, input_size])
            output_images.append(draw_prediction_on_image(
                image[frame_idx, :, :, :].numpy().astype(np.int32),
                keypoints_with_scores, crop_region=None,
                close_figure=True, output_image_height=300))
            crop_region = determine_crop_region(
                keypoints_with_scores, image_height, image_width)
            bar.update(progress(frame_idx, num_frames - 1))

        # Prepare gif visualization.
        output = np.stack(output_images, axis=0)
        resulfGif = to_gif(output, fps=10)

        clip = VideoFileClip(resulfGif)
        resultMp4 = 'A' + dist_name + '.mp4'
        clip.write_videofile(resultMp4)
        mp4Link = uploadMp4(resultMp4)

        line_bot_api.reply_message(
            event.reply_token,
            VideoSendMessage(
                original_content_url=mp4Link,
                preview_image_url=mp4Link
            )
        )'''
        if lineID == dao.selectForUser('user', 'id'):
            userContact = dao.selectForUser('user', 'contactPerson')
        elif lineID == dao.selectForUser('trainer', 'id'):
            userContact = dao.selectForUser('trainer', 'contacter')
        else:
            userContact = '0'

        if userContact != '0':
            if msg != '結束會議':
                trainerLineId = userContact

                line_bot_api.push_message(
                    trainerLineId,
                    TextSendMessage(
                        text=msg
                    )
                )
            else:
                dao.updateTrainerContacter('0', userContact)
                dao.updateTableForUser('user', 'contactPerson', '0')

                msgCont = [
                    TextSendMessage(
                        text='會議已結束'
                    ),
                    TextSendMessage(
                        text='來對教練留下你的分數以及評論吧'
                    ),
                    TextSendMessage(
                        text='分數區間在1~5 輸入範例如下'
                    ),
                    TextSendMessage(
                        text='分數:5'
                    ),
                    TextSendMessage(
                        text='評論:good!'
                    )
                ]

                line_bot_api.reply_message(
                    event.reply_token,
                    msgCont
                )

        elif msg == 'entry':
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text='hello',
                    contents=bot_entry
                )
            )

        elif msg == '以用戶身份加入':

            dao.insertLineIdToUserAndBodyType()

            msgList = [
                TextSendMessage(
                    text='請輸入您的姓名'
                ),
                TextSendMessage(
                    text='並請以特定格式輸入 在你要輸入的名稱前加入 姓名：'
                ),
                TextSendMessage(
                    text='範例  姓名：王小明'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgList
            )
        elif msg == '以教練身份加入':

            dao.insertLineIdToTrainerAndReservation()

            msgList = [
                TextSendMessage(
                    text='請輸入您的姓名'
                ),
                TextSendMessage(
                    text='並請以特定格式輸入 在你要輸入的名稱前加入 教練:'
                ),
                TextSendMessage(
                    text='範例  教練:王小明'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgList
            )

        elif msg[0:3] == '姓名：':
            userName = msg[3:]

            dao.updateTableForUser('user', 'name', userName)

            msgList = [
                TextSendMessage(
                    text='請輸入您的身高'
                ),
                TextSendMessage(
                    text='並請以特定格式輸入 在你要輸入的身高前加入 身高：'
                ),
                TextSendMessage(
                    text='範例  身高：170'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgList
            )

        elif msg[0:3] == '教練：':
            trainerName = msg[3:]
            dao.updateTableForUser('trainer', 'trainerName', trainerName)

            msgList = [
                TextSendMessage(
                    text='請輸入您的服務區域'
                ),
                TextSendMessage(
                    text='並請以特定格式輸入 在你要輸入的區域前加入 區域：'
                ),
                TextSendMessage(
                    text='範例  區域:台北'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgList
            )

        elif msg[0:3] == '區域：':
            area = msg[3:]
            dao.updateTableForUser('trainer', 'area', area)

            msgList = [
                TextSendMessage(
                    text='請輸入您的服務時間 建議在(8:00~13:00之間)'
                ),
                TextSendMessage(
                    text='並請以特定格式輸入 在你要輸入的時間前加入 時間：'
                ),
                TextSendMessage(
                    text='範例  時間:8:00 ~13:00'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgList
            )

        elif msg[0:3] == '時間：':
            serviceTime = msg[3:]
            dao.updateTableForUser('trainer', 'serviceHour', serviceTime)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text='請上傳一張個人的照片'
                )
            )

        elif msg[0:3] == '身高：':
            userHeight = msg[3:]

            dao.updateTableForUser('user', 'height', userHeight)

            msgConts = [
                TextSendMessage(
                    text='請上傳一張你的全身照'
                ),
                TextSendMessage(
                    text='我們可以透過你上傳的照片進行身形的推估及計算，來為你達到個人化的推薦!'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgConts
            )

        elif msg == 'isjpg':
            image_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(3)) + '.jpg'
            imagePath = '/usr/local/forTest/photo/'+image_name
            message_content = line_bot_api.get_message_content(event.message.id)
            with open(imagePath, 'wb') as fd:
                for chunk in message_content.iter_content():
                    fd.write(chunk)

            ID = dao.selectForUser('user', 'id')

            if ID == lineID:

                dao.updateTableForUser('user', 'imageLocation', imagePath)
                height = dao.selectForUser('user', 'height')

                command = 'python3 /home/hduser/IdeaProjects/py37measurement/Human-Body-Measurements-using-Computer-Vision/inference.py -i '
                command = command + str(imagePath) + ' -ht ' + str(height)
                # os.system(command)
                kaf(command)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='等30秒'
                    )
                )

                time.sleep(40)

                f = open('/usr/local/forTest/temp/'+image_name+'_'+str(height), 'r')
                measurements = f.read()
                bodyPart = str(measurements).split(',')

                shoulderWidth = bodyPart[8].split(':')[1]
                chest = bodyPart[3].split(':')[1]
                waist = bodyPart[1].split(':')[1]
                hips = bodyPart[9].split(':')[1]
                f.close()

                dao.updateTableForUser('bodyType', 'shoulderWidth', float(shoulderWidth))
                dao.updateTableForUser('bodyType', 'chest', float(chest))
                dao.updateTableForUser('bodyType', 'waist', float(waist))
                dao.updateTableForUser('bodyType', 'hips', float(hips))

                measurement = Measurement(float(shoulderWidth), float(height), float(chest), float(waist), float(hips))
                measurement.calculateBodyType()

                dao.updateTableForUser('bodyType', 'bodyType', str(measurement.getBodyType())[0])

                line_bot_api.push_message(
                    lineID,
                    FlexSendMessage(
                        alt_text='hello',
                        contents=measurement.getBodyType_json()
                    )
                )

            else:
                imgur_client_id ='487d15d96e787f5'

                title = "Uploaded with PyImgur"


                reservationList = []

                for i in range(1, 8):
                    reservation = Reservation(lineID, '選')
                    times = str(7+i)+':00~'+str(8+i)+':00'
                    reservation.setButton(times, i)
                    reservationList.append(reservation)

                reservation = Reservation(lineID, '選')
                reservation.setReturnButton('endToChoicePeriod')
                reservationList.append(reservation)

                reservationLists = Lists(reservationList)

                msgCont = [
                    FlexSendMessage(
                        alt_text='newMessage',
                        contents=reservationLists.getReservationJson()
                    ),
                    TextSendMessage(
                        text='請選擇可服務的時間 當選擇完畢時請按返回'
                    )
                ]

                line_bot_api.reply_message(
                    event.reply_token,
                    msgCont
                )

                im = pyimgur.Imgur(imgur_client_id)

                uploaded_image = im.upload_image(imagePath, title=title)
                time.sleep(3)
                dao.updateTableForUser('trainer', 'imageLocation', str(uploaded_image.link))

        elif msg == '建議飲食':

            waist = dao.selectForUser('bodyType', 'waist')
            hips = dao.selectForUser('bodyType', 'hips')

            if float(waist)/float(hips) >= 0.95:
                call_bubble_or_carousel(fatJson)
            elif float(waist)/float(hips) < 0.8:
                call_bubble_or_carousel(thinJson)
            else:
                call_bubble_or_carousel(normalJson)

        elif msg == 'myBodyType':

            height = dao.selectForUser('user', 'height')
            shoulderWidth = dao.selectForUser('bodyType', 'shoulderWidth')
            chest = dao.selectForUser('bodyType', 'chest')
            waist = dao.selectForUser('bodyType', 'waist')
            hips = dao.selectForUser('bodyType', 'hips')

            measurement = Measurement(float(shoulderWidth), float(height), float(chest), float(waist), float(hips))
            measurement.calculateBodyType()

            call_bubble_or_carousel(measurement.getBodyType_json())
        elif msg[0:3] == '選時段':

            time_serial = msg[3]
            reservationList = []
            col = 'timePeriod'+str(time_serial)

            dao.updateTableForTrainer('reservation', col, 'T')
            rows = dao.selectTimePeriodByTrainerId(lineID)
            for row in rows:
                # row[i] = time period
                for i in range(1, 8):
                    reservation = Reservation(lineID, '選')
                    if row[i] != 'T':
                        times = str(7+i)+':00~'+str(8+i)+':00'
                        reservation.setButton(times, i)
                        reservationList.append(reservation)

            reservation = Reservation(lineID, '選')
            reservation.setReturnButton('endToChoicePeriod')
            reservationList.append(reservation)

            reservationLists = Lists(reservationList)
            msgCont = [
                FlexSendMessage(
                    alt_text='newMessage',
                    contents=reservationLists.getReservationJson()
                ),
                TextSendMessage(
                    text='請選擇可服務的時間 當選擇完畢時請按返回'
                )
            ]

            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg == 'endToChoicePeriod':
            msgCont = [
                FlexSendMessage(
                    alt_text='newMsg',
                    contents=bot_teachBodyType_json
                ),
                TextSendMessage(
                    text='請選擇擅長教學的體型'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg[1:4] == '型身材':
            body_type = msg[0]
            rows = dao.selectCourseByBodyType(body_type)

            poseList = []

            for row in rows:

                trainerId = row[0]

                trainerIds = str(trainerId).split(',')

                if lineID in trainerIds:
                    continue

                poseName = row[2]
                poseBodyPart = row[3]
                equipment = row[4]
                difficulty = row[5]
                imageUrl = row[6]

                pose = Pose()
                pose.setPoseImage(imageUrl).setPoseName(poseName).setPoseBodyPart(poseBodyPart)
                pose.setPoseEquipment(equipment).setPoseDifficulty(difficulty).setAddCoachButton(poseName, body_type)

                poseList.append(pose)

            courseCarousel = Carousel(poseList)

            return_button = Return()
            return_button.setReturnLabel('結束')
            return_button.setReturnText('trainerEnd')

            msgCont = [
                FlexSendMessage(
                    alt_text='newMsg',
                    contents=courseCarousel.getJson()
                ),
                FlexSendMessage(
                    alt_text='newMsg',
                    contents=return_button.getReturnJson()
                )
            ]

            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg[0:8] == 'newCoach':
            body_type = msg[8]
            pose_name = msg[9:]
            rows = dao.selectTrainerIdByTypeAndPose(body_type, pose_name)

            originalId = []
            for row in rows:
                originalId.append(row[0])

            dao.addTrainerIdToCourse(originalId[0], body_type, pose_name, lineID)

            returnButt = Return()

            returnButt.setReturnText(str(body_type)+'型身材')

            msgCont = [
                TextSendMessage(
                    text='新增成功!'
                ),
                FlexSendMessage(
                    alt_text='newMsg',
                    contents=returnButt.getReturnJson()
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg[0:4] == '建議課表':

            bodyType = dao.selectForUser('bodyType', 'bodyType')
            rows = dao.selectCourseByBodyType(bodyType)

            poseList = []

            for row in rows:

                trainerId = row[0]
                poseName = row[2]
                poseBodyPart = row[3]
                equipment = row[4]
                difficulty = row[5]
                imageUrl = row[6]

                pose = Pose()
                pose.setPoseImage(imageUrl).setPoseName(poseName).setPoseBodyPart(poseBodyPart)
                pose.setPoseEquipment(equipment).setPoseDifficulty(difficulty).setRecommendButton(poseName)

                poseList.append(pose)

            courseCarousel = Carousel(poseList)
            call_bubble_or_carousel(courseCarousel.getJson())

        elif msg[0:4] == '推薦教練':
            pose_name = msg[4:]
            bodyType = dao.selectForUser('bodyType', 'bodyType')
            rows = dao.selectTrainerIdByTypeAndPose(bodyType, pose_name)

            for row in rows:
                trainerIds = row[0]

            trainerIdList = str(trainerIds).split(',')

            trainerList = []

            for i in range(0, len(trainerIdList)):
                coachId = trainerIdList[i]
                trainerData = dao.selectAllByTrainerId(coachId)
                for row in trainerData:
                    trainerName = row[1]
                    trainerImageURL = row[2]
                    trainerArea = row[3]
                    serviceHour = row[4]

                member = Member()
                member.setTrainerImage(trainerImageURL).setTrainerName(trainerName).setTrainerArea(trainerArea)
                member.setTrainerServiceHour(serviceHour).setButtonTrainerEvaluation('教練評價*'+str(pose_name)+'*'+str(coachId))
                member.setButtonContactTrainer('聯絡教練'+str(coachId))

                trainerList.append(member)

            coachCarousel = Carousel(trainerList)
            call_bubble_or_carousel(coachCarousel.getJson())

        elif msg[0:4] == '教練評價':
            message = msg.split('*')
            poseName = message[1]
            coachId = message[2]

            commentsOnCoach = dao.selectCommentByTrainerId(coachId)

            commentList = []

            for row in commentsOnCoach:
                userName = row[1]
                score = row[2]
                commentText = row[3]

                comment = Comment()
                comment.setCommentUserName(userName).setCommentScore(score).setCommentText(commentText)
                commentList.append(comment)

            commentCarousel = Carousel(commentList)
            call_bubble_or_carousel(interface_json=commentCarousel.getJson())

            returnButton = Return()
            returnButton.setReturnText('推薦教練'+poseName)
            line_bot_api.push_message(
                lineID,
                FlexSendMessage(
                    alt_text='newMessage',
                    contents=returnButton.getReturnJson()
                )
            )

        elif msg[0:4] == '聯絡教練':
            coachId = msg[4:]

            contact = Contact()
            contact.setContactByTextReturn('文字訊息訂單'+str(coachId))
            contact.setContactByMeetingReturn('線上會議訂單'+'Uc2ccc8c3f2bf4b981019abeaefaaab52')
            call_bubble_or_carousel(contact.getContactOptionJson())

        # 跳出預約時間表
        elif msg[0:6] == '文字訊息訂單' or msg[0:6] == '線上會議訂單':
            if msg[0:6] == '文字訊息訂單':
                coachId = msg[6:]
                contactTypeWord = '文'
            else:
                coachId = msg[6:]
                contactTypeWord = '線'

            reservationList = []

            rows = dao.selectTimePeriodByTrainerId(coachId)
            for row in rows:
                # row[i] = time period
                for i in range(1, 8):
                    reservation = Reservation(coachId, contactTypeWord)
                    if row[i] == 'T':
                        times = str(7+i)+':00~'+str(8+i)+':00'
                        reservation.setButton(times, i)
                        reservationList.append(reservation)

            reservation = Reservation(coachId, contactTypeWord)
            reservation.setReturnButton('聯絡教練'+str(coachId))
            reservationList.append(reservation)

            reservationLists = Lists(reservationList)

            msgCont = [
                TextSendMessage(
                    text='請選擇日期'
                ),
                FlexSendMessage(
                    alt_text='newMessage',
                    contents=reservationLists.getReservationJson()
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg[1:3] == '時段':
            contactType = msg[0]
            serial = msg[3]
            coachId = msg[4:]

            startHour = int(serial)+7

            timestamp = str(event.timestamp)
            timestamp = timestamp[0:10]
            times = Times(int(timestamp))

            remainSec = times.getRemainSecond(startHour)

            if contactType == '線':

                contact = Contact()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='請稍後當預約時間到了將會自動傳連結'
                    )
                )

                print(remainSec)
                # time.sleep(remainSec)

                contact.generateMeetingRoom()

                msgCont = [
                    TextSendMessage(
                        text='請在30秒內加入 之後系統將會允許加入會議'
                    ),
                    FlexSendMessage(
                        alt_text='newMessage',
                        contents=contact.getGoogleMeetJson()
                    )
                ]

                line_bot_api.push_message(
                    lineID,
                    msgCont
                )
                # to coach
                line_bot_api.push_message(
                    coachId,
                    msgCont
                )
                contact.allowUserJoinMeeting()
                # contact.setTimeToCloseMeeting(remainTime=3)

                msgCont = [
                    TextSendMessage(
                        text='來對教練留下你的分數以及評論吧'
                    ),
                    TextSendMessage(
                        text='分數區間在1~5 輸入範例如下'
                    ),
                    TextSendMessage(
                        text='分數:5'
                    ),
                    TextSendMessage(
                        text='評論:good!'
                    )
                ]

                usrName = dao.selectForUser('user', 'name')

                print('coachId', coachId)
                print('usrName', usrName)
                dao.insertUsrNameAndIdToComment(usrName, coachId)

                line_bot_api.push_message(
                    lineID,
                    msgCont
                )

            # for 文字訊息
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='請稍後當預約時間到了將會傳送通知'
                    )
                )

                # time.sleep(remainSec)

                usrName = dao.selectForUser('user', 'name')
                coachName = dao.selectForTrainer('trainer', 'trainerName', coachId)

                order1 = Order()
                order2 = Order()
                order1.setTrainerName(coachName).setStartButtonReturn('startPushWith'+str(coachId))

                order2.setTrainerName(usrName)

                line_bot_api.push_message(
                    lineID,
                    FlexSendMessage(
                        alt_text='newMessage',
                        contents=order1.getOrderJson()
                    )
                )
                # to coach
                line_bot_api.push_message(
                    coachId,
                    FlexSendMessage(
                        alt_text='newMessage',
                        contents=order1.getOrderJson()
                    )
                )

        elif msg[0:2] == '分數' or msg[0:2] == '評論':
            usrName = dao.selectForUser('user', 'name')

            if msg[0:2] == '分數':
                scores = msg[3:]
                dao.updateComment(score=scores, usrName=usrName)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='收到你的評分了 快來留下你的評論吧！'
                    )
                )
            elif msg[0:2] == '評論':
                comments = msg[3:]
                dao.updateComment(comment=comments, usrName=usrName)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='感謝你的參與！！'
                    )
                )
                dao.updateTableForUser('user', 'contactPerson', '0')

        elif msg[0:13] == 'startPushWith':
            coachId = msg[13:]
            dao.updateTableForUser('user', 'contactPerson', str(coachId))
            dao.updateTrainerContacter(lineID, coachId)

            coachName = dao.selectForTrainer('trainer', 'trainerName', coachId)

            textMsg = '可以開始與{}傳送文字'
            textMsg = textMsg.format(coachName)

            msgCont = [
                TextSendMessage(
                    text=textMsg
                ),
                TextSendMessage(
                    text='要離開會議時請輸入 結束會議'
                )
            ]

            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

        elif msg == 'trainerEnd':
            msgCont = [
                TextSendMessage(
                    text='感謝使用！'
                ),
                TextSendMessage(
                    text='當有用戶選擇你的課程會在通知你！！'
                )
            ]
            line_bot_api.reply_message(
                event.reply_token,
                msgCont
            )

    return HttpResponseBadRequest()




