from googleapiclient.discovery import build
import streamlit as st
import yaml
with open("config.yaml", "r") as f:
    params = yaml.safe_load(f)

def get_youtube_service():
    api_key = params['GOOGLE_API_KEY']
    return build("youtube", "v3", developerKey=api_key)

def search_videos(query, max_results=5):
    youtube = get_youtube_service()
    request = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results
    )
    response = request.execute()
    return response['items'] if 'items' in response else []

def get_video_stats(video_id):
    youtube = get_youtube_service()
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['statistics'] if 'items' in response else None

def app():
    st.title("YouTube Search Analytics")
    search_query = st.text_input("Enter Search Query:")
    
    if search_query:
        st.subheader(f"Results for '{search_query}':")
        search_results = search_videos(search_query)
        
        for result in search_results:
            video_id = result['id']['videoId']
            title = result['snippet']['title']
            description = result['snippet']['description']
            
            stats = get_video_stats(video_id)
            views = stats['viewCount'] if stats else "N/A"
            likes = stats['likeCount'] if stats else "N/A"

            st.write(f"**Title:** {title}")
            st.write(f"**Video ID:** {video_id}")
            st.write(f"**Description:** {description}")
            st.write(f"**Views:** {views}")
            st.write(f"**Likes:** {likes}")
            st.markdown("---")
