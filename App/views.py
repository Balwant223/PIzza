from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializer
from rest_framework.parsers import JSONParser 

    

@api_view(['GET','POST'])
def pizzas_list(request):
    if request.method=='GET':
        pizzas=Pizza.objects.all()
        serializer=PizzaSerializer(pizzas,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=request.data
        print(data)
        if len(list(data.keys()))==1 and list(data.keys())[0]=='Type':
            pizzas=Pizza.objects.filter(Type=data['Type'])
            serializer=PizzaSerializer(pizzas,many=True)
            if serializer.data:
                return Response(serializer.data)
            else:
                return Response({"Object Does Not exist":data['Type']},status.HTTP_404_NOT_FOUND)
        elif len(list(data.keys()))==1 and list(data.keys())[0]=='Size':
            pizzas=Pizza.objects.filter(Size=data['Size'])
            serializer=PizzaSerializer(pizzas,many=True)
            if serializer.data:
                return Response(serializer.data)
            else:
                return Response({"Object Does Not exist":data['Size']},status.HTTP_404_NOT_FOUND)
        return Response({"Your key must be Type or Size":"Your Value"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_pizza(request):
    if request.method=='POST':
        serializer=PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def alter_pizza(request,id):
    try: 
        pizza = Pizza.objects.get(id=id) 
    except Pizza.DoesNotExist: 
        return Response({'message': 'The Pizza does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        pizza_data=JSONParser().parse(request)
        serializer=PizzaSerializer(pizza,data=pizza_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        pizza.delete() 
        return Response({'message': 'Pizza was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)