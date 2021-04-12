from django.shortcuts import render
from rest_framework.response import Response
from django.db import connection
from .serializers import *
from rest_framework.decorators import api_view
import datetime

@api_view(['POST', 'GET'])
def userDetails(request):
    try:
        if request.method == 'POST':

            serializer = userDetailsSerializer(data=request.data)

            if serializer.is_valid():
                firstname = serializer['firstname'].value
                lastname = serializer['lastname'].value
                email = serializer['email'].value
                address1 = serializer['address1'].value
                address2 = serializer['address2'].value
                address3 = serializer['address3'].value

                if firstname and email and address1:
                    with connection.cursor() as cursor:
                        cursor.execute(''' Select * from datatable where FirstName = %s ''', [firstname])

                        if cursor.rowcount > 0:
                            if lastname and address2 and address3:
                                result = cursor.execute(''' Update datatable set FirstName = %s, LastName = %s, Email = %s, Address1 = %s, Address2 = %s, Address3 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, lastname, email, address1, address2, address3, datetime.datetime.now(), firstname])
                            elif lastname and address2:
                                result = cursor.execute(''' Update datatable set FirstName = %s, LastName = %s, Email = %s, Address1 = %s, Address2 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, lastname, email, address1, address2, datetime.datetime.now(), firstname]) 
                            elif address2 and address3:
                                result = cursor.execute(''' Update datatable set FirstName = %s, Email = %s, Address1 = %s, Address2 = %s, Address3 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, email, address1, address2, address3, datetime.datetime.now(), firstname])
                            elif address2:
                                result = cursor.execute(''' Update datatable set FirstName = %s, Email = %s, Address1 = %s, Address2 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, email, address1, address2, datetime.datetime.now(), firstname])
                            elif lastname:
                                result = cursor.execute(''' Update datatable set FirstName = %s, LastName = %s, Email = %s, Address1 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, lastname, email, address1, datetime.datetime.now(), firstname])
                            else:
                                result = cursor.execute(''' Update datatable set FirstName = %s, Email = %s, Address1 = %s, UpdatedAt = %s where FirstName = %s ''', [firstname, email, address1, datetime.datetime.now(), firstname])

                            if result:
                                return Response({'Message': 'User data Updated successfully'})
                            else:
                                return Response({'Message': 'User data Not Updated successfully'})

                        else:
                            if lastname and address2 and address3:
                                result = cursor.execute(''' Insert into datatable(FirstName, LastName, Email, Address1, Address2, Address3, CreatedAt) Values (%s, %s, %s, %s, %s, %s, %s) ''', [firstname, lastname, email, address1, address2, address3, datetime.datetime.now()])
                            elif lastname and address2:
                                result = cursor.execute(''' Insert into datatable(FirstName, LastName, Email, Address1, Address2, CreatedAt) Values (%s, %s, %s, %s, %s, %s) ''', [firstname, lastname, email, address1, address2, datetime.datetime.now()])
                            elif address2 and address3:
                                result = cursor.execute(''' Insert into datatable(FirstName, Email, Address1, Address2, Address3, CreatedAt) Values (%s, %s, %s, %s, %s, %s) ''', [firstname, email, address1, address2, address3, datetime.datetime.now()]) 
                            elif address2:
                                result = cursor.execute(''' Insert into datatable(FirstName, Email, Address1, Address2, CreatedAt) Values (%s, %s, %s, %s, %s) ''', [firstname, email, address1, address2, datetime.datetime.now()])                        
                            elif lastname:
                                result = cursor.execute(''' Insert into datatable(FirstName, LastName, Email, Address1, CreatedAt) Values (%s, %s, %s, %s, %s) ''', [firstname, lastname, email, address1, datetime.datetime.now()])
                            else:
                                result = cursor.execute(''' Insert into datatable(FirstName, Email, Address1, CreatedAt) Values (%s, %s, %s, %s) ''', [firstname, email, address1, datetime.datetime.now()])

                            if result:
                                return Response({'Message': 'User data Inserted successfully'})
                            else:
                                return Response({'Message': 'User data Not Inserted successfully'})

                else:
                    return Response({'Message': 'Mandatory fields required'})

            else:
                return Response({'Message': 'Some field is empty'})

        elif request.method == 'GET':
            with connection.cursor() as cursor:
                cursor.execute(''' SELECT * from datatable ''')
                if cursor.rowcount > 0:
                    return Response(dictfetchall(cursor))
                else:
                    return Response({'data': 'No data found'})

    except Exception as e:
        print(e)
        return Response({'Message': 'Some error occured'})

def dictfetchall(cursor = ''):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]