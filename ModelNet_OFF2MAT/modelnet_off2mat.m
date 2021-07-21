function modelnet_off2mat(off_path, data_path, classes, volume_size, angle_inc)
% Put the mesh object in a volume grid and save the volumetric
% represenation file.
% This is the input volumetric data for 3D ShapeNets.
% off_path: root off data folder
% data_path: destination volumetric data folder

phases = {'train', 'test'};

% data_size = pad_size * 2 + volume_size;
for c = 1:length(classes)
    fprintf('writing the %s category\n', classes{c});
    category_path = [off_path '\' classes{c}];
    dest_path = [data_path '\' classes{c} '\'];
    if ~exist(dest_path, 'dir')
        mkdir(dest_path);
    end
    % for train and test phases
    for t = 1 
        %: numel(phases)
        phase = phases{t};
        off_list = [category_path '\' phase];
        dest_ts_path = [dest_path '\' phase];
        if ~exist(dest_ts_path, 'dir')
            mkdir(dest_ts_path);
        end
       
        files = dir(off_list);
        for i = 3 : length(files)
            fprintf('total is %d file', length(files));
            fprintf('   writing the %d th file\n', i);
            if strcmp(files(i).name, '.') || strcmp(files(i).name, '..') || files(i).isdir == 1 || ~strcmp(files(i).name(end-2:end), 'off')
                continue;
            end
%             rnd_Vol = randi([0 4]);
            
            filename = [off_list '\' files(i).name];
            dest_tsdf_path = [dest_ts_path '\' files(i).name];
            if ~exist(dest_tsdf_path, 'dir')
                mkdir(dest_tsdf_path);
            end
        
            for phi=[-30,30]
                for viewpoint = 1:360/angle_inc
                    
                    destname = [dest_tsdf_path '\' files(i).name(1:end-4) '_' num2str(viewpoint) '_' num2str(phi)  '.mat'];
                    off_data = off_loader(filename, (viewpoint-1)*angle_inc,phi);
%                 instance = polygon2voxel(off_data, [volume_size, volume_size, volume_size], 'auto',t,rnd_Vol);
                    instance = polygon2voxel(off_data, [volume_size, volume_size, volume_size], 'auto');
%                 instance = padarray(instance, [pad_size, pad_size, pad_size]);
                    instance = int8(instance);
                    save(destname, 'instance');
                end
            end
        end
    end
end


function offobj = off_loader(filename, theta, phi, axis, stretch)

offobj = struct();
fid = fopen(filename, 'rb');
OFF_sign = fscanf(fid, '%c', 3);
assert(strcmp(OFF_sign, 'OFF') == 1);

info = fscanf(fid, '%d', 3);
offobj.vertices = reshape(fscanf(fid, '%f', info(1)*3), 3, info(1))';
offobj.faces = reshape(fscanf(fid, '%d', info(2)*4), 4, info(2))';
len=size(offobj.faces,1);
% do some translation and rotation
center=(sum(offobj.vertices(offobj.faces(2,:)+1,:))/len+sum(offobj.vertices(offobj.faces(3,:)+1,:))/len+sum(offobj.vertices(offobj.faces(4,:)+1,:))/len);
%center = (max(offobj.vertices) + min(offobj.vertices)) / 2;
offobj.vertices = bsxfun(@minus, offobj.vertices, center);
if exist('axis', 'var')
    switch axis
        case 'x'
            offobj.vertices(:,1) = offobj.vertices(:,1) * stretch;
        case 'y'
            offobj.vertices(:,2) = offobj.vertices(:,2) * stretch;
        case 'z'
            offobj.vertices(:,3) = offobj.vertices(:,3) * stretch;
        otherwise
            error('off_loader axis set wrong');
    end
end
theta = theta * pi / 180;
phi=phi*pi/180;
R1 = [cos(theta), -sin(theta), 0;
     sin(theta), cos(theta) , 0;
        0      ,    0       , 1];

R2=[1,0,0;
    0,cos(phi), -sin(phi);
     0,sin(phi), cos(phi);];
offobj.vertices = offobj.vertices * R1*R2;

% These vertices to define faces should be offset by one to follow the matlab convention.
offobj.faces = offobj.faces(:,2:end) + 1; 

fclose(fid);
