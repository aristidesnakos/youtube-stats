from googleapiclient.discovery import build
import streamlit as st
import matplotlib.pyplot as plt
from search_page import get_youtube_service,get_video_stats
def get_channel_info(query, max_results=5):
    youtube = get_youtube_service()
    request = youtube.search().list(
        q=query,
        type="channel",
        order="viewCount", # Sorting by popularity
        part="id,snippet",
        maxResults=max_results
    )
    response = request.execute()
    return response['items'] if 'items' in response else []

def app():
    st.title("Channel & Video Stats")

    # Channel Subscribers
    channel_id = st.text_input("Enter Channel ID:")
    if channel_id:
        channel_info = get_channel_info(channel_id)
        if channel_info:
            st.write(f"Subscribers for channel {channel_info['snippet']['title']}:")
            st.write(channel_info['statistics']['subscriberCount'])
    
    # Views Per Video
    search_query = st.text_input("Enter Search Query for Video Views:")
    if search_query:
        video_id = st.text_input("Enter Video ID from Search Query:")
        if video_id:
            video_stats = get_video_stats(video_id)
            if video_stats:
                views = video_stats['viewCount']
                st.write(f"Views for video ID {video_id}:")
                st.write(views)
                fig, ax = plt.subplots()
                ax.bar(['Views'], [views])
                st.pyplot(fig)
