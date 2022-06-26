
# subject = " edit your Transction successfully"
# message = '''
#     edit your Trancation with new Inofrmation \n
#     Amount: {} \n in Category {} \n
#     description is: {} \n
#     Last date Update: {}
#     '''.format(request.POST['amount'], request.POST['category'], request.POST['desc'],
#                 datetime.datetime.now())

# email_from = settings.EMAIL_HOST_USER
# user = User.objects.get(id=profiles.id)
# recipient_list = [user.email, ]
# send_mail(subject, message, email_from,
#             recipient_list,  fail_silently=False,)
