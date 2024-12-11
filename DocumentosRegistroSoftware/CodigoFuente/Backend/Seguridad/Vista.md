```
//ENTITY VISTA
package com.persona.Backend.Entity.Security;

import com.persona.Backend.Entity.BaseEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "vista")
public class Vista extends BaseEntity {

	@Column(name = "nombre", length = 100, nullable = false, unique = true)
	private String nombre;

	@Column(name = "descripcion", length = 100, nullable = true)
	private String descripcion;

	@Column(name = "ruta", length = 70, nullable = false, unique= true)
	private String ruta;
	
	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "modulo_id", nullable = false, unique = false)
	private Modulo moduloId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Modulo getModuloId() {
		return moduloId;
	}

	public void setModuloId(Modulo moduloId) {
		this.moduloId = moduloId;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public String getRuta() {
		return ruta;
	}

	public void setRuta(String ruta) {
		this.ruta = ruta;
	}



}
// IREPOSITORY VISTA 
package com.persona.Backend.IRepository.Security;

import java.util.Optional;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Security.Vista;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IVistaRepository extends IBaseRepository<Vista, Long> {
	
	Optional<Vista> findByNombre(String nombre);

}
// ISERVICE VISTA 
package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.Vista;
import com.persona.Backend.IService.IBaseService;

public interface IVistaService extends IBaseService<Vista> {

	 Vista findByNombre(String nombre);
}
//SERVICE VISTA
package com.persona.Backend.Service.Security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.Vista;
import com.persona.Backend.IRepository.Security.IVistaRepository;
import com.persona.Backend.IService.Security.IVistaService;
import com.persona.Backend.Service.BaseService;

@Service
public class VistaService extends BaseService<Vista> implements IVistaService{

	@Autowired
    private IVistaRepository vistaRepository;
	
	@Override
    public Vista findByNombre(String nombre) {
        return vistaRepository.findByNombre(nombre).orElse(null);
    }
	
}
//CONTROLLER VISTA
package com.persona.Backend.Controller.Security;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.Vista;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/vista")
public class VistaController extends BaseController<Vista> {

}


```