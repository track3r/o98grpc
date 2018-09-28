# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import other98_pb2 as other98__pb2


class TheOther98Stub(object):
  """TheOther98 service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeed = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/GetFeed',
        request_serializer=other98__pb2.FeedRequest.SerializeToString,
        response_deserializer=other98__pb2.FeedResponseView.FromString,
        )
    self.GetPost = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/GetPost',
        request_serializer=other98__pb2.GetRequest.SerializeToString,
        response_deserializer=other98__pb2.PostView.FromString,
        )
    self.GetProfile = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/GetProfile',
        request_serializer=other98__pb2.GetRequest.SerializeToString,
        response_deserializer=other98__pb2.ProfileResponseView.FromString,
        )
    self.CreatePost = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/CreatePost',
        request_serializer=other98__pb2.CreatePostRequest.SerializeToString,
        response_deserializer=other98__pb2.Result.FromString,
        )
    self.CreateComment = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/CreateComment',
        request_serializer=other98__pb2.Comment.SerializeToString,
        response_deserializer=other98__pb2.Result.FromString,
        )
    self.VoteOnPost = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/VoteOnPost',
        request_serializer=other98__pb2.PostVote.SerializeToString,
        response_deserializer=other98__pb2.Result.FromString,
        )
    self.VoteOnComment = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/VoteOnComment',
        request_serializer=other98__pb2.CommentVote.SerializeToString,
        response_deserializer=other98__pb2.Result.FromString,
        )
    self.PopulateDatabase = channel.unary_unary(
        '/com.fanreact.other98.TheOther98/PopulateDatabase',
        request_serializer=other98__pb2.Void.SerializeToString,
        response_deserializer=other98__pb2.Void.FromString,
        )


class TheOther98Servicer(object):
  """TheOther98 service definition.
  """

  def GetFeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProfile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VoteOnPost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VoteOnComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PopulateDatabase(self, request, context):
    """demo methods
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TheOther98Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeed,
          request_deserializer=other98__pb2.FeedRequest.FromString,
          response_serializer=other98__pb2.FeedResponseView.SerializeToString,
      ),
      'GetPost': grpc.unary_unary_rpc_method_handler(
          servicer.GetPost,
          request_deserializer=other98__pb2.GetRequest.FromString,
          response_serializer=other98__pb2.PostView.SerializeToString,
      ),
      'GetProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GetProfile,
          request_deserializer=other98__pb2.GetRequest.FromString,
          response_serializer=other98__pb2.ProfileResponseView.SerializeToString,
      ),
      'CreatePost': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePost,
          request_deserializer=other98__pb2.CreatePostRequest.FromString,
          response_serializer=other98__pb2.Result.SerializeToString,
      ),
      'CreateComment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateComment,
          request_deserializer=other98__pb2.Comment.FromString,
          response_serializer=other98__pb2.Result.SerializeToString,
      ),
      'VoteOnPost': grpc.unary_unary_rpc_method_handler(
          servicer.VoteOnPost,
          request_deserializer=other98__pb2.PostVote.FromString,
          response_serializer=other98__pb2.Result.SerializeToString,
      ),
      'VoteOnComment': grpc.unary_unary_rpc_method_handler(
          servicer.VoteOnComment,
          request_deserializer=other98__pb2.CommentVote.FromString,
          response_serializer=other98__pb2.Result.SerializeToString,
      ),
      'PopulateDatabase': grpc.unary_unary_rpc_method_handler(
          servicer.PopulateDatabase,
          request_deserializer=other98__pb2.Void.FromString,
          response_serializer=other98__pb2.Void.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.fanreact.other98.TheOther98', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
