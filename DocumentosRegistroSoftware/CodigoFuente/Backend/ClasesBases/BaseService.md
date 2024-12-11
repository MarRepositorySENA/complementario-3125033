```
//SERVICE IBASESERVICE
package com.persona.Backend.Service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.IRepository.IBaseRepository;
import com.persona.Backend.IService.IBaseService;
import com.persona.Backend.Utils.GlobalConstants;

@Service
public abstract class BaseService<T extends BaseEntity> implements IBaseService<T> {
	@Autowired
	private IBaseRepository<T, Long> repository;

	@Autowired
	private AuditoriaService auditService;

	@Override
	public List<T> all() throws Exception {
		return repository.findAll();
	}

	@Override
	public Optional<T> findById(Long id) throws Exception {
		return repository.findById(id);
	}

	@Override
	public T save(T instanceEntity) throws Exception {
		if (instanceEntity.getCreatedAt() == null) {
			auditService.setAuditOnCreate(instanceEntity);
		} else {
			auditService.setAuditOnUpdate(instanceEntity);
		}
		return repository.save(instanceEntity);
	}

	@Override
	public void update(Long id, T instanceEntity) throws Exception {
	    Optional<T> optionalP = this.repository.findById(id);
	    if (optionalP.isEmpty()) {
	        throw new Exception("No se encontró registro");
	    }
	    T objetoToUpdate = optionalP.get();

	    // Aseguramos que el campo `createdAt` no sea sobrescrito
	    instanceEntity.setCreatedAt(objetoToUpdate.getCreatedAt());

	    // Copiamos las demás propiedades, excluyendo las que no deben cambiar
	    BeanUtils.copyProperties(instanceEntity, objetoToUpdate,
	            GlobalConstants.EXCLUDED_FIELDS.toArray(new String[0]));

	    auditService.setAuditOnUpdate(objetoToUpdate);  // Aseguramos que la auditoría se actualice
	    this.repository.save(objetoToUpdate);
	}


	@Override
	public void delete(Long id) throws Exception {
		Optional<T> optionalP = this.repository.findById(id);
		if (optionalP.isEmpty()) {
			throw new Exception("No se encontró registro");
		}
		T objetoToDelete = optionalP.get();
		auditService.setAuditOnDelete(objetoToDelete);
		this.repository.save(objetoToDelete);
	}

	@Override
	public List<T> findByDeletedAtIsNullAndStateTrue() {
		return repository.findByDeletedAtIsNullAndStateTrue();
	}

	@Override
	public List<T> findByDeletedAtIsNull() {
		return repository.findByDeletedAtIsNull();
	}
}

//SERVICE AUDITORIASERVICE

package com.persona.Backend.Service;

import java.time.LocalDateTime;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.BaseEntity;

@Service
public class AuditoriaService {

    // Método para configurar auditoría al crear la entidad
    public void setAuditOnCreate(BaseEntity entity) {
        entity.setCreatedAt(LocalDateTime.now()); // Asigna la fecha de creación
        entity.setUpdatedAt(LocalDateTime.now()); // Asigna la fecha de actualización inicial
        entity.setState(true);                    // Asigna el estado a true
        entity.setDeletedAt(null);                // Asegura que deletedAt sea null al crear
    }

    // Método para configurar auditoría al actualizar la entidad
    public void setAuditOnUpdate(BaseEntity entity) {
        entity.setUpdatedAt(LocalDateTime.now()); // Actualiza la fecha de actualización
        // No se modifica createdAt ni deletedAt
    }

    // Método para configurar auditoría al eliminar la entidad
    public void setAuditOnDelete(BaseEntity entity) {
        entity.setDeletedAt(LocalDateTime.now()); // Asigna la fecha de eliminación
        entity.setState(false);                   // Cambia el estado a false (desactivado)
    }
}

```