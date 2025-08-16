# https://huggingface.co/spaces/kunalpro379/tts
# text to Audio API

pip install gradio_client


from gradio_client import Client

client = Client("kunalpro379/tts")
result = client.predict(
		text="Hello!!",
		language="mar",
		api_name="/predict"
)
print(result)


