```
//ENTIDAD CONTINENTE
package com.persona.Backend.Entity.Parameter.Ubicacion;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "continente")
public class Continente extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

}
// IREPOSITORY CONTINENTE
package com.persona.Backend.IRepository.Parameter.Ubicacion;

import java.util.Optional;

import org.springframework.stereotype.Repository;
import com.persona.Backend.Entity.Parameter.Ubicacion.Continente;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IContinenteRepository extends IBaseRepository<Continente, Long> {

	Optional<Continente> findByNombre(String nombre);
}
//ISERVICE CONTINENTE
package com.persona.Backend.IService.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Continente;
import com.persona.Backend.IService.IBaseService;

public interface IContinenteService extends IBaseService<Continente>{
	
	Continente findByNombre(String nombre);

}
//SERVICE CONTINENTE
package com.persona.Backend.Service.Parameter.Ubicacion;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Ubicacion.Continente;
import com.persona.Backend.IRepository.Parameter.Ubicacion.IContinenteRepository;
import com.persona.Backend.IService.Parameter.Ubicacion.IContinenteService;
import com.persona.Backend.Service.BaseService;
import java.util.List;

@Service
public class ContinenteService extends BaseService<Continente> implements IContinenteService {

	@Autowired
	private IContinenteRepository continenteRepository;

	@Override
	public Continente findByNombre(String nombre) {
		return continenteRepository.findByNombre(nombre).orElse(null);
	}
}
//CONTROLLER CONTINENTE
package com.persona.Backend.Controller.Parameter.Ubicacion;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Ubicacion.Continente;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/ubicacion/continente")
public class ContinenteController extends BaseController<Continente>{

}



```