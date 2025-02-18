# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import proxy_pb2 as proxy__pb2


class ProxyEngineServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ServerVersionGet = channel.unary_unary(
        '/imrpc.ProxyEngineService/ServerVersionGet',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineVersionProxyResponse.FromString,
        )
    self.VolumeGet = channel.unary_unary(
        '/imrpc.ProxyEngineService/VolumeGet',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineVolumeGetProxyResponse.FromString,
        )
    self.VolumeExpand = channel.unary_unary(
        '/imrpc.ProxyEngineService/VolumeExpand',
        request_serializer=proxy__pb2.EngineVolumeExpandRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.VolumeFrontendStart = channel.unary_unary(
        '/imrpc.ProxyEngineService/VolumeFrontendStart',
        request_serializer=proxy__pb2.EngineVolumeFrontendStartRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.VolumeFrontendShutdown = channel.unary_unary(
        '/imrpc.ProxyEngineService/VolumeFrontendShutdown',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.VolumeSnapshot = channel.unary_unary(
        '/imrpc.ProxyEngineService/VolumeSnapshot',
        request_serializer=proxy__pb2.EngineVolumeSnapshotRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineVolumeSnapshotProxyResponse.FromString,
        )
    self.SnapshotList = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotList',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotListProxyResponse.FromString,
        )
    self.SnapshotRevert = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotRevert',
        request_serializer=proxy__pb2.EngineSnapshotRevertRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotPurge = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotPurge',
        request_serializer=proxy__pb2.EngineSnapshotPurgeRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotPurgeStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotPurgeStatus',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotPurgeStatusProxyResponse.FromString,
        )
    self.SnapshotClone = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotClone',
        request_serializer=proxy__pb2.EngineSnapshotCloneRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotCloneStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotCloneStatus',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotCloneStatusProxyResponse.FromString,
        )
    self.SnapshotRemove = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotRemove',
        request_serializer=proxy__pb2.EngineSnapshotRemoveRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotHash = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotHash',
        request_serializer=proxy__pb2.EngineSnapshotHashRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotHashStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotHashStatus',
        request_serializer=proxy__pb2.EngineSnapshotHashStatusRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotHashStatusProxyResponse.FromString,
        )
    self.SnapshotBackup = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotBackup',
        request_serializer=proxy__pb2.EngineSnapshotBackupRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotBackupProxyResponse.FromString,
        )
    self.SnapshotBackupStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/SnapshotBackupStatus',
        request_serializer=proxy__pb2.EngineSnapshotBackupStatusRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineSnapshotBackupStatusProxyResponse.FromString,
        )
    self.BackupRestore = channel.unary_unary(
        '/imrpc.ProxyEngineService/BackupRestore',
        request_serializer=proxy__pb2.EngineBackupRestoreRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineBackupRestoreProxyResponse.FromString,
        )
    self.BackupRestoreStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/BackupRestoreStatus',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineBackupRestoreStatusProxyResponse.FromString,
        )
    self.ReplicaAdd = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaAdd',
        request_serializer=proxy__pb2.EngineReplicaAddRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReplicaList = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaList',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineReplicaListProxyResponse.FromString,
        )
    self.ReplicaRebuildingStatus = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaRebuildingStatus',
        request_serializer=proxy__pb2.ProxyEngineRequest.SerializeToString,
        response_deserializer=proxy__pb2.EngineReplicaRebuildStatusProxyResponse.FromString,
        )
    self.ReplicaVerifyRebuild = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaVerifyRebuild',
        request_serializer=proxy__pb2.EngineReplicaVerifyRebuildRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReplicaRemove = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaRemove',
        request_serializer=proxy__pb2.EngineReplicaRemoveRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReplicaModeUpdate = channel.unary_unary(
        '/imrpc.ProxyEngineService/ReplicaModeUpdate',
        request_serializer=proxy__pb2.EngineReplicaModeUpdateRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ProxyEngineServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ServerVersionGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeExpand(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeFrontendStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeFrontendShutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeSnapshot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotRevert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotPurge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotPurgeStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotClone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotCloneStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotRemove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHashStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotBackup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotBackupStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupRestore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupRestoreStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaAdd(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaRebuildingStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaVerifyRebuild(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaRemove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaModeUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProxyEngineServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ServerVersionGet': grpc.unary_unary_rpc_method_handler(
          servicer.ServerVersionGet,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineVersionProxyResponse.SerializeToString,
      ),
      'VolumeGet': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeGet,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineVolumeGetProxyResponse.SerializeToString,
      ),
      'VolumeExpand': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeExpand,
          request_deserializer=proxy__pb2.EngineVolumeExpandRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'VolumeFrontendStart': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeFrontendStart,
          request_deserializer=proxy__pb2.EngineVolumeFrontendStartRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'VolumeFrontendShutdown': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeFrontendShutdown,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'VolumeSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeSnapshot,
          request_deserializer=proxy__pb2.EngineVolumeSnapshotRequest.FromString,
          response_serializer=proxy__pb2.EngineVolumeSnapshotProxyResponse.SerializeToString,
      ),
      'SnapshotList': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotList,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotListProxyResponse.SerializeToString,
      ),
      'SnapshotRevert': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotRevert,
          request_deserializer=proxy__pb2.EngineSnapshotRevertRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotPurge': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotPurge,
          request_deserializer=proxy__pb2.EngineSnapshotPurgeRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotPurgeStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotPurgeStatus,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotPurgeStatusProxyResponse.SerializeToString,
      ),
      'SnapshotClone': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotClone,
          request_deserializer=proxy__pb2.EngineSnapshotCloneRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotCloneStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotCloneStatus,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotCloneStatusProxyResponse.SerializeToString,
      ),
      'SnapshotRemove': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotRemove,
          request_deserializer=proxy__pb2.EngineSnapshotRemoveRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotHash': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHash,
          request_deserializer=proxy__pb2.EngineSnapshotHashRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotHashStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHashStatus,
          request_deserializer=proxy__pb2.EngineSnapshotHashStatusRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotHashStatusProxyResponse.SerializeToString,
      ),
      'SnapshotBackup': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotBackup,
          request_deserializer=proxy__pb2.EngineSnapshotBackupRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotBackupProxyResponse.SerializeToString,
      ),
      'SnapshotBackupStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotBackupStatus,
          request_deserializer=proxy__pb2.EngineSnapshotBackupStatusRequest.FromString,
          response_serializer=proxy__pb2.EngineSnapshotBackupStatusProxyResponse.SerializeToString,
      ),
      'BackupRestore': grpc.unary_unary_rpc_method_handler(
          servicer.BackupRestore,
          request_deserializer=proxy__pb2.EngineBackupRestoreRequest.FromString,
          response_serializer=proxy__pb2.EngineBackupRestoreProxyResponse.SerializeToString,
      ),
      'BackupRestoreStatus': grpc.unary_unary_rpc_method_handler(
          servicer.BackupRestoreStatus,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineBackupRestoreStatusProxyResponse.SerializeToString,
      ),
      'ReplicaAdd': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaAdd,
          request_deserializer=proxy__pb2.EngineReplicaAddRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReplicaList': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaList,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineReplicaListProxyResponse.SerializeToString,
      ),
      'ReplicaRebuildingStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaRebuildingStatus,
          request_deserializer=proxy__pb2.ProxyEngineRequest.FromString,
          response_serializer=proxy__pb2.EngineReplicaRebuildStatusProxyResponse.SerializeToString,
      ),
      'ReplicaVerifyRebuild': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaVerifyRebuild,
          request_deserializer=proxy__pb2.EngineReplicaVerifyRebuildRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReplicaRemove': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaRemove,
          request_deserializer=proxy__pb2.EngineReplicaRemoveRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReplicaModeUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaModeUpdate,
          request_deserializer=proxy__pb2.EngineReplicaModeUpdateRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imrpc.ProxyEngineService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
