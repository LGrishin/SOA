import grpc
import post_api_pb2
import post_api_pb2_grpc
import concurrent
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('DATABASE_LOCATION'))
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(String)

Base.metadata.create_all(engine)

class PostsServicer(post_api_pb2_grpc.PostsServicer):
    def AddPost(self, request: post_api_pb2.AddPostRequest, context: grpc.ServicerContext):
        user_id = request.user_id
        content = request.content
        Session = sessionmaker(bind=engine)
        session = Session()
        new_post = Post(user_id=user_id, content=content)
        post_id = new_post.post_id
        session.add(new_post)
        session.commit()
        session.close()
        return post_api_pb2.AddPostResponse(post_id)

    def DeletePost(self, request, context):
        user_id = request.user_id
        post_id = request.post_id
        Session = sessionmaker(bind=engine)
        session = Session()
        post = session.query(Post).filter_by(user_id=user_id, post_id=post_id).first()
        
        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("The post of this user was not found")
            return post_api_pb2.DeletePostResponse(success=False)
        
        session.delete(post)
        session.commit()
        session.close()
        return post_api_pb2.DeletePostResponse(success=True)
    
    def UpdatePost(self, request, context):
        user_id = request.user_id
        post_id = request.post_id
        new_content = request.new_content
        Session = sessionmaker(bind=engine)
        session = Session()
        
        post = session.query(Post).filter_by(user_id=user_id, post_id=post_id).first()
        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("The post of this user was not found")
            return post_api_pb2.UpdatePostResponse(success=False)
        
        post.content = new_content
        session.commit()
        session.close()
        return post_api_pb2.UpdatePostResponse(success=True)
    
    def GetPost(self, request, context):
        post_id = request.post_id
        Session = sessionmaker(bind=engine)
        session = Session()
        post = session.query(Post).filter_by(post_id=post_id).first()
        if not post:
            return post_api_pb2.GetPostResponse(success=False, content='')
        content = post.content
        session.close()
        return post_api_pb2.GetPostResponse(success=True, content=content)

    def GetPosts(self, request, context):
        number_of_posts = request.number_of_posts
        offset = request.offset
        Session = sessionmaker(bind=engine)
        session = Session()
        posts = session.query(Post).offset(offset).limit(number_of_posts).all()
        session.close()
    
        result = []
        for post in posts:
            response = post_api_pb2.GetPostResponse(success=True, content=post.content)
            result.append(response)
        return post_api_pb2.GetPostsResponse(result)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    post_api_pb2_grpc.add_PostsServicer_to_server(PostsServicer(), server)
    server.add_insecure_port('0.0.0.0:'+ str(os.environ["POST_SERV_PORT"]))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
