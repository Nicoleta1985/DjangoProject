from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from professor.form import ProfessorForm
from professor.models import Professor
from professor.serializers import ProfesorSerializer


class ProfessorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'professor/create_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('home')
    permission_required = 'professor.add_professor'


class ProfessorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'professor/list_of_professors.html'
    model = Professor
    context_object_name = 'all_professors'
    permission_required = 'professor.view_list_of_professors'

    def get_queryset(self):
        return Professor.objects.filter(active=True)


class ProfessorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'professor/update_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('list_of_professors')
    permission_required = 'professor.change_professor'


class ProfessorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'professor/delete_professor.html'
    model = Professor
    success_url = reverse_lazy('list_of_professors')
    permission_required = 'professor.delete_professor'


class ProfessorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'professor/details_professor.html'
    model = Professor
    permission_required = 'professor.view_professor'


@login_required
@permission_required('inactivate_professor')
def inactivate_professor(request, pk):
    Professor.objects.filter(id=pk).update(active=False)
    return redirect('list_of_professors')


@login_required
@permission_required('delete_professor_modal')
def delete_professor(request,pk):
    Professor.objects.filter(id=pk).delete()
    return redirect('list_of_professors')

#API - application programming interface -> este utilizat pentru a transmite bidirectional
# date intre aplicatii software intr-un  mod formalizat


class ProfessorAPIView(APIView):

    def get(self, request):
        queryset = Professor.objects.all() #sau filter(active=True)
        serializer = ProfesorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorPKApiView(APIView):

    def put(self, request, pk):
        queryset = Professor.objects.get(id=pk)
        serializer = ProfesorSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = Professor.objects.get(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        queryset = Professor.objects.get(id=pk)
        serializer = ProfesorSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

