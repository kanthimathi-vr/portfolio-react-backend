import json
from django.http import JsonResponse
from .models import ContactMessage  # Import your model

def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not all([name, email, message]):
                return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)

            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            return JsonResponse({'success': True, 'message': 'Message stored successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format.'}, status=400)

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'}, status=500)

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
