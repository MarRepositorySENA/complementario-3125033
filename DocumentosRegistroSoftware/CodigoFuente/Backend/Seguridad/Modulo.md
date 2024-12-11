```
//ENTIDAD MODULO
package com.persona.Backend.Entity.Security;

import com.persona.Backend.Entity.BaseEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "modulo")
public class Modulo extends BaseEntity {

	@Column(name = "nombre", length = 45)
	private String nombre;
	
	@Column(name = "ruta", length = 50)
	private String ruta;
	
	@Column(name = "icono", length = 50)
	private String icono;
	
	@ManyToOne
    @JoinColumn(name = "padre_id", nullable = true)
    private Modulo padreId;

	

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getRuta() {
		return ruta;
	}

	public void setRuta(String ruta) {
		this.ruta = ruta;
	}

	public String getIcono() {
		return icono;
	}

	public void setIcono(String icono) {
		this.icono = icono;
	}

	

}
//IREPOSITORY MODULO
package com.persona.Backend.IRepository.Security;

import java.util.Optional;

import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.persona.Backend.Dto.DataSelectDto;
import com.persona.Backend.Entity.Security.Modulo;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IModuloRepository extends IBaseRepository<Modulo, Long>{

	@Query(value = "select "
			+ "id, "
			+ "name as TextoMostrar "
			+ "From"
			+ "Modulo "
			+ "WHERE deleted_at is NULL AND estado=1 "
			+ "ORDER BY id ASC ", nativeQuery=true)
	Optional<DataSelectDto> SeleccionarDatos(Long id);
	
	
	 Optional<Modulo> findByNombre(String nombre);
}

//ISERVICE MODULO
package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.Modulo;
import com.persona.Backend.IService.IBaseService;

public interface IModuloService extends IBaseService<Modulo> {

	Modulo findByNombre(String nombre);
}
//SERVICE MODULO
package com.persona.Backend.Service.Security;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.Modulo;
import com.persona.Backend.IRepository.Security.IModuloRepository;
import com.persona.Backend.IService.Security.IModuloService;
import com.persona.Backend.Service.BaseService;

@Service
public class ModuloService extends BaseService<Modulo> implements IModuloService {
	
	 @Autowired
	    private IModuloRepository moduloRepository;
	
	 @Override
	    public Modulo findByNombre(String nombre) {
	        return moduloRepository.findByNombre(nombre).orElse(null);
	    }

	
	
	
}
//CONTROLLER MODULO

package com.persona.Backend.Controller.Security;



import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.Modulo;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/modulo")
public class ModuloController  extends BaseController<Modulo>{

}



```