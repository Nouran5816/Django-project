from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile, SecretData

class ProfileFetchView(APIView):
   
    def post(self, request):
        try:
            if 'name' not in request.data:
                data = {
                'message': 'Please provide valid data',
                'status': 'error',
               
                }
                return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
            obj_data = Profile.objects.get(name=request.data['name'])
            obj_data = ProfileSerializer(obj_data).data
            data = {
                'message': 'Profile created successfully',
                'status': 'success',
                "data":obj_data
               
            }
            return JsonResponse(data)
        except:
            data = {
                'message': 'Failed to create post',
                'status': 'error',
               
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
   
    def post(self, request):
        print(request.data)
        username_in = request.data['name']
       # import pdb
       #pdb.set_trace()
        prof  = Profile.objects.filter(name = username_in).values('name','number')
        print(prof)
        data = {
            'message': 'Profile created successfully',
            'status': 'success',
            'profiles':  prof 
            }
        return Response({"profiles": prof})
        
        
    '''
    print(request.data)
        username_in = request.data['username']
        prof  = Profile.objects.filter(username = username_in).delete()
        print(prof)
        data = {
            'message': 'Profile deleted successfully',
            'status': 'success'
            }
        return Response({"action": data})
    
    def post(self, request):
        try:
            
            if not('name' in request.data and request.data['name'] != ""):
                data = {
                    'message': 'Please provide valid data',
                    'status': 'error',
                
                }
                return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

            data = request.data
            secret_obj = SecretData.objects.get(key="testingkey")
            secret_id = secret_obj.uid
            data['secret_id'] =  secret_id
            obj = Profile.objects.create(**data) #create object in db
            obj.save()
            # data = {
            #     'message': 'Profile created successfully',
            #     'status': 'success',
               
            # }
            # return JsonResponse(data)
            obj_data = Profile.objects.get(id=obj.pk) #fetching the obj from db
            obj_data = ProfileSerializer(obj_data).data #serlizer the obj thats featched --
            data = {
                'message': 'Profile created successfully',
                'status': 'success',
                "data":obj_data
               
            }  
            return JsonResponse(data)
        except:
            data = {
                'message': 'Failed to create post',
                'status': 'error',
               
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)'''