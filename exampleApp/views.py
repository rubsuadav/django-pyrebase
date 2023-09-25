from rest_framework import views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .firebase import firestore
from .validators import validate_data
from google.cloud.firestore_v1 import Query


class CsrfExemptMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class JobView(CsrfExemptMixin, views.APIView):
    def get(self, request, job_id=''):
        page = self.request.query_params.get('page')

        if job_id == '':
            if page:  # Get jobs with pagination (4 jobs per page)
                try:
                    page = int(page)
                    if int(page) < 1:  # Check if page is less than 1
                        return Response({"error": "Page must be greater or equal than 1"}, status=400)
                except Exception as e:
                    return Response({"error": "Page must be an integer"}, status=400)
                jobs = firestore.collection(u'jobs').order_by(
                    u'company', direction=Query.DESCENDING).limit(4).offset((int(page) - 1) * 4).stream()
                return Response([doc.to_dict() for doc in jobs], status=200)
            else:  # Get all jobs without pagination
                jobs = firestore.collection(
                    u'jobs').order_by(u'company').stream()
                return Response([doc.to_dict() for doc in jobs], status=200)
        else:  # Get job by id
            job = firestore.collection(u'jobs').document(str(job_id)).get()
            if job.exists:  # Check if job exists
                job = job.to_dict()
                return Response(job, status=200)
            else:
                return Response({"error": "Job not found"}, status=404)

    def post(self, request):
        token = request.headers.get('Bearer')
        job = request.data
        if not token:
            return Response({"error": "Token login is missing, you must login first and put the token on the header request"}, status=400)
        try:
            validate_data(job)
            company = job.get("company")
            title = job.get("title")
            location = job.get("location")

            firestore.collection(u'jobs').document().set({
                u'company': company,
                u'title': title,
                u'location': location
            })
            return Response({"message": "Job added successfully"}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)
