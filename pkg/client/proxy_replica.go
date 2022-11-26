package client

import (
	"context"
	"github.com/pkg/errors"

	rpc "github.com/longhorn/longhorn-instance-manager/pkg/imrpc"

	etypes "github.com/longhorn/longhorn-engine/pkg/types"
	eptypes "github.com/longhorn/longhorn-engine/proto/ptypes"
)

func (c *ProxyClient) ReplicaAdd(ctx context.Context, serviceAddress, replicaAddress string, restore bool, size, currentSize int64) (err error) {
	input := map[string]string{
		"serviceAddress": serviceAddress,
		"replicaAddress": replicaAddress,
	}
	if err := validateProxyMethodParameters(input); err != nil {
		return errors.Wrap(err, "failed to add replica for volume")
	}

	defer func() {
		if restore {
			err = errors.Wrapf(err, "%v failed to add restore replica %v for volume", c.getProxyErrorPrefix(serviceAddress), replicaAddress)
		} else {
			err = errors.Wrapf(err, "%v failed to add replica %v for volume", c.getProxyErrorPrefix(serviceAddress), replicaAddress)
		}
	}()

	req := &rpc.EngineReplicaAddRequest{
		ProxyEngineRequest: &rpc.ProxyEngineRequest{
			Address: serviceAddress,
		},
		ReplicaAddress: replicaAddress,
		Restore:        restore,
		Size:           size,
		CurrentSize:    currentSize,
	}
	_, err = c.service.ReplicaAdd(getContextWithGRPCLongTimeout(ctx), req)
	if err != nil {
		return err
	}

	return nil
}

func (c *ProxyClient) ReplicaList(ctx context.Context, serviceAddress string) (rInfoList []*etypes.ControllerReplicaInfo, err error) {
	input := map[string]string{
		"serviceAddress": serviceAddress,
	}
	if err := validateProxyMethodParameters(input); err != nil {
		return nil, errors.Wrap(err, "failed to list replicas for volume")
	}

	defer func() {
		err = errors.Wrapf(err, "%v failed to list replicas for volume", c.getProxyErrorPrefix(serviceAddress))
	}()

	req := &rpc.ProxyEngineRequest{
		Address: serviceAddress,
	}
	resp, err := c.service.ReplicaList(getContextWithGRPCTimeout(ctx), req)
	if err != nil {
		return nil, err
	}

	for _, cr := range resp.ReplicaList.Replicas {
		rInfoList = append(rInfoList, &etypes.ControllerReplicaInfo{
			Address: cr.Address.Address,
			Mode:    eptypes.GRPCReplicaModeToReplicaMode(cr.Mode),
		})
	}

	return rInfoList, nil
}

func (c *ProxyClient) ReplicaRebuildingStatus(ctx context.Context, serviceAddress string) (status map[string]*ReplicaRebuildStatus, err error) {
	input := map[string]string{
		"serviceAddress": serviceAddress,
	}
	if err := validateProxyMethodParameters(input); err != nil {
		return nil, errors.Wrap(err, "failed to get replicas rebuilding status")
	}

	defer func() {
		err = errors.Wrapf(err, "%v failed to get replicas rebuilding status", c.getProxyErrorPrefix(serviceAddress))
	}()

	req := &rpc.ProxyEngineRequest{
		Address: serviceAddress,
	}
	recv, err := c.service.ReplicaRebuildingStatus(getContextWithGRPCTimeout(ctx), req)
	if err != nil {
		return status, err
	}

	status = make(map[string]*ReplicaRebuildStatus)
	for k, v := range recv.Status {
		status[k] = &ReplicaRebuildStatus{
			Error:              v.Error,
			IsRebuilding:       v.IsRebuilding,
			Progress:           int(v.Progress),
			State:              v.State,
			FromReplicaAddress: v.FromReplicaAddress,
		}
	}
	return status, nil
}

func (c *ProxyClient) ReplicaVerifyRebuild(ctx context.Context, serviceAddress, replicaAddress string) (err error) {
	input := map[string]string{
		"serviceAddress": serviceAddress,
		"replicaAddress": replicaAddress,
	}
	if err := validateProxyMethodParameters(input); err != nil {
		return errors.Wrap(err, "failed to verify replica rebuild")
	}

	defer func() {
		err = errors.Wrapf(err, "%v failed to verify replica %v rebuild", c.getProxyErrorPrefix(serviceAddress), replicaAddress)
	}()

	req := &rpc.EngineReplicaVerifyRebuildRequest{
		ProxyEngineRequest: &rpc.ProxyEngineRequest{
			Address: serviceAddress,
		},
		ReplicaAddress: replicaAddress,
	}
	_, err = c.service.ReplicaVerifyRebuild(getContextWithGRPCTimeout(ctx), req)
	if err != nil {
		return err
	}

	return nil
}

func (c *ProxyClient) ReplicaRemove(ctx context.Context, serviceAddress, replicaAddress string) (err error) {
	input := map[string]string{
		"serviceAddress": serviceAddress,
		"replicaAddress": replicaAddress,
	}
	if err := validateProxyMethodParameters(input); err != nil {
		return errors.Wrap(err, "failed to remove replica for volume")
	}

	defer func() {
		err = errors.Wrapf(err, "%v failed to remove replica %v for volume", c.getProxyErrorPrefix(serviceAddress), replicaAddress)
	}()

	req := &rpc.EngineReplicaRemoveRequest{
		ProxyEngineRequest: &rpc.ProxyEngineRequest{
			Address: serviceAddress,
		},
		ReplicaAddress: replicaAddress,
	}
	_, err = c.service.ReplicaRemove(getContextWithGRPCTimeout(ctx), req)
	if err != nil {
		return err
	}

	return nil
}
