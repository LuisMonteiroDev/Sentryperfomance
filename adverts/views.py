from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from .models import Adverts, AdvertsViewed, AdvertsBooks, AdvertsBookViewed
from .serializers import AdvertsSerializers, AdvertsViewedSerializers, AdvertsBooksSerializers, AdvertsBooksViewedSerializers
from users.models import Users
from library.models import Librarys
from adminUsibras.models import Books
from datetime import datetime

from utils import send_email


class AdvertsViewSet(ModelViewSet):
    queryset = Adverts.objects.all()
    serializer_class = AdvertsSerializers
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def create_announcement(self, request):
        user = request.user
        data = request.data
        try:
            library = Librarys.objects.get(id=data['library_id'])
            if user in library.owner_library.all():
                create_at = datetime.strptime(data['create_at'], '%d/%m/%Y %H:%M')
                expiration = datetime.strptime(data['expiration'], '%d/%m/%Y %H:%M')
                if create_at >= expiration:
                    return Response({'message': 'A data de criação do anúncio não pode ser maior/igual a data de expiração!'},
                                    status=status.HTTP_400_BAD_REQUEST)
                Adverts.objects.create(
                    announcement=data['announcement'],
                    library_id=library.id,
                    description=data['description'],
                    create_at=create_at,
                    expiration=expiration
                )
                return Response({'message': 'Anúncio criado com sucesso!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Somente o(s) usuário(s) dono(s) desta biblioteca pode(m) criar anúncios!'},
                                status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            return Response({'message': 'Biblioteca anunciante não encontrada!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao criar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def list_adverts(self, request):
        now = datetime.now()
        try:
            adverts = Adverts.objects.filter(create_at__lte=now, expiration__gte=now)
            serializer = AdvertsSerializers(adverts, many=True)
            return Response({'message': 'Anúncios encontrados', 'adverts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncios!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated])
    def update_announcement(self, request):
        user = request.user
        data = request.data
        try:
            update_announcement = Adverts.objects.get(id=data['announcement_id'])
            if user in update_announcement.library.owner_library.all():
                create_at = datetime.strptime(data['create_at'], '%d/%m/%Y %H:%M')
                expiration = datetime.strptime(data['expiration'], '%d/%m/%Y %H:%M')
                if create_at >= expiration:
                    return Response({'message': 'A data de criação do anúncio não pode ser maior/igual a data de expiração!'},
                                    status=status.HTTP_400_BAD_REQUEST)
                update_announcement.announcement = data['announcement']
                update_announcement.create_at = create_at
                update_announcement.expiration = expiration
                update_announcement.save()
                return Response({'message': 'Anúncio atualizado com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Somente o(s) usuário(s) dono(s) desta biblioteca pode(m) atualizar anúncios!'},
                                status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            return Response({'message': 'Anúncio não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao atualizar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def advert_by_id(self, request):
        params = request.query_params
        now = datetime.now()
        try:
            advert = Adverts.objects.get(id=params['advert_id'], create_at__lte=now, expiration__gte=now)
            serializer = AdvertsSerializers(advert)
            return Response({'message': 'Anúncio encontrado', 'advert': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'Anúncio não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['DELETE'], permission_classes=[IsAuthenticated])
    def delete_advert(self, request):
        params = request.query_params
        user = request.user
        now = datetime.now()
        try:
            advert = Adverts.objects.get(id=params['advert_id'], create_at__lte=now, expiration__gte=now)
            if user not in advert.library.owner_library.all():
                return Response({'message': 'Somente o(s) usuário(s) dono(s) desta biblioteca pode(m) atualizar anúncios!'},
                    status=status.HTTP_403_FORBIDDEN)
            else:
                advert.delete()
                return Response({'message': 'Anúncio deletado com sucesso'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'Anúncio não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdvertsViewedViewSet(ModelViewSet):
    queryset = AdvertsViewed.objects.all()
    serializer_class = AdvertsSerializers
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def register_view(self, request):
        user = request.user
        data = request.data
        now = datetime.now()
        try:
            announcement = Adverts.objects.get(id=data['announcement_id'], create_at__lte=now, expiration__gte=now)
            AdvertsViewed.objects.create(
                user_viewed_id=user.id,
                announcement_id=announcement.id,
                date=now
            )
            return Response({'message': 'Anúncio visualizado com sucesso'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'anúncio não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao visualizar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def number_advert_views(self, request):
        params = request.query_params
        now = datetime.now()
        try:
            announcement_id = Adverts.objects.get(id=params['announcement_id'], create_at__lte=now, expiration__gte=now)
            announcement = AdvertsViewed.objects.filter(announcement_id=announcement_id).count()
            serializer = AdvertsSerializers(announcement_id)
            return Response({
                'message': 'Quantidades de vezes que o anúncio foi visto',
                'views': announcement,
                'announcement': serializer.data
            }, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'anúncio não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar quantidade de vezes que anúncio foi visto!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def list_all_adverts_views(self, request):
        try:
            adverts = AdvertsViewed.objects.all()
            serializer = AdvertsViewedSerializers(adverts, many=True)
            return Response({'message': 'Anúncios visualizados', 'adverts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncios!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdvertsBooksViewSet(ModelViewSet):
    queryset = AdvertsBooks.objects.all()
    serializer_class = AdvertsBooksSerializers
    permission_classes = IsAuthenticated

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def create_announcement_book(self, request):
        user = request.user
        data = request.data
        try:
            book = Books.objects.get(id=data['book_id'])
            if user in book.available_in_libraries.owner_library.all():
                create_at = datetime.strptime(data['create_at'], '%d/%m/%Y %H:%M')
                expiration = datetime.strptime(data['expiration'], '%d/%m/%Y %H:%M')
                if create_at >= expiration:
                    return Response(
                        {'message': 'A data de criação do anúncio não pode ser maior/igual a data de expiração!'},
                        status=status.HTTP_400_BAD_REQUEST)

                ad = AdvertsBooks.objects.create(
                    announcement=data['announcement'],
                    book_id=book.id,
                    description=data['description'],
                    create_at=create_at,
                    expiration=expiration
                )
                users = Users.objects.all()
                for user in users:
                    if book in user.favorite_books.all():
                        send_email(
                            user.email,
                            'Novo anúncio de um de seus livros favoritos!',
                            f'Livro {book} - Descrição do anúncio: {ad.description}'
                        )

                return Response({'message': 'Anúncio criado com sucesso!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Somente o(s) usuário(s) dono(s) desta biblioteca pode(m) criar anúncios!'},
                                status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            return Response({'message': 'Livro anunciante não encontrada!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao criar anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def list_adverts_books(self, request):
        now = datetime.now()
        try:
            adverts = AdvertsBooks.objects.filter(create_at__lte=now, expiration__gte=now)
            serializer = AdvertsBooksSerializers(adverts, many=True)
            return Response({'message': 'Anúncios encontrados', 'adverts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncios!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def list_adverts_by_book(self, request):
        params = request.query_params
        now = datetime.now()
        try:
            book = AdvertsBooks.objects.filter(book_id=params['book_id'])
            serializer = AdvertsBooksSerializers(book, many=True)
            return Response({'message': 'Anúncios sobre o livro encontrados', 'book_adverts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao listar anúncios!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def register_view_book(self, request):
        user = request.user
        data = request.data
        now = datetime.now()
        try:
            AdvertsBookViewed.objects.create(
                user_viewed_id=user.id,
                announcement_id=data['announcement_book_id'],
                date=now
            )
            return Response({'message': 'Visualização registrada com sucesso'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao registrar visualização!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def count_views_adverts_book(self, request):
        params = request.query_params
        now = datetime.now()
        try:
            announcement = AdvertsBooks.objects.get(id=params['announcement_book_id'], create_at__lte=now, expiration__gte=now)
            announcement_viewed = AdvertsBookViewed.objects.filter(announcement_id=params['announcement_book_id']).count()
            serializer = AdvertsBooksSerializers(announcement)
            return Response({
                'message': 'Quantidades de vezes que o anúncio foi visto',
                'views': announcement_viewed,
                'announcement': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'message': 'Erro ao contar número de visualizações do anúncio!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

